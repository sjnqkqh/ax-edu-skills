"""
운송사 청구서 PDF 및 현장 인수증 JPG 수작업 대조 재현 스크립트
스마트폰 촬영 노이즈(임의 각도 회전, 원근/거리 편차, 조명 음영)가 포함된 바이너리 서류를 열어 내용을 판독하고,
내부 배차 일지와 대조하는 현장 실무자의 4단계 수작업 프로세스(읽기 -> 나누기 -> 찾아보기 -> 초안)를 시뮬레이션합니다.
"""
import os
import csv
import re
from PIL import Image
import fitz  # PyMuPDF

def extract_invoice_data_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = doc[0].get_text()
    doc.close()
    
    v_match = re.search(r"(\d{2}가\d{4})", text)
    v_no = v_match.group(1) if v_match else "차량번호미상"
    
    route_match = re.search(r"([가-힣0-9A-Za-z]+)\s*→\s*([가-힣0-9A-Za-z]+)", text)
    route = f"{route_match.group(1)}->{route_match.group(2)}" if route_match else "구간미상"
    
    amounts = re.findall(r"([\d,]+)\s*원", text)
    cleaned_amounts = [int(a.replace(",", "")) for a in amounts]
    
    claimed_base = cleaned_amounts[0] if len(cleaned_amounts) >= 1 else 0
    claimed_surcharge = cleaned_amounts[1] if len(cleaned_amounts) >= 2 else 0
    total_claim = cleaned_amounts[2] if len(cleaned_amounts) >= 3 else (claimed_base + claimed_surcharge)
    
    surcharge_name = "해당없음"
    if "야간운행할증" in text:
        surcharge_name = "야간운행할증"
    elif "하차대기할증" in text:
        surcharge_name = "하차대기할증"
        
    return {
        "vehicle_no": v_no,
        "route": route,
        "claimed_base": claimed_base,
        "claimed_surcharge": claimed_surcharge,
        "total_claim": total_claim,
        "surcharge_name": surcharge_name
    }

def inspect_receipt_photo(jpg_path):
    with Image.open(jpg_path) as img:
        w, h = img.size
        # 코너 픽셀 색상으로 원거리(책상 배경) 여부 감지
        corner_color = img.getpixel((5, 5))
        is_desk_bg = (corner_color[0] < 200 and corner_color[1] < 200)
        
        # 가로세로 비율로 회전/기울임 대략적 감지
        aspect = w / h
        if aspect > 1.4:
            orientation = "정방향 수평 촬영"
        elif aspect < 0.7:
            orientation = "90도/270도 수직 회전 촬영"
        else:
            orientation = "30도~60도 비스듬한 기울기 촬영"

        distance_desc = "원거리 촬영 (작업대 바닥 배경 노출)" if is_desk_bg else "근접/표준 촬영"
        
        return {
            "size": (w, h),
            "orientation": orientation,
            "distance": distance_desc
        }

def run_simulation():
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, "data")
    inbox_csv = os.path.join(data_dir, "day_inbox.csv")
    lookup_csv = os.path.join(data_dir, "dispatch_lookup.csv")

    if not os.path.exists(inbox_csv) or not os.path.exists(lookup_csv):
        print(f"[오류] 필수 데이터 파일이 없습니다: {data_dir}")
        return

    dispatch_map = {}
    with open(lookup_csv, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dispatch_map[row["vehicle_no"]] = row

    total_count = 0
    matched_count = 0
    rework_count = 0
    tilted_scans_count = 0

    print("=" * 85)
    print(" [물류/회계] 비정형 바이너리(PDF 청구서 + 스마트폰 현장 촬영 JPG 인수증) 수작업 대조 시작")
    print("=" * 85)

    with open(inbox_csv, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for item in reader:
            total_count += 1
            inv_no = item["invoice_no"]
            carrier = item["carrier_name"]
            pdf_rel = item["pdf_path"]
            rcp_rel = item["receipt_path"]
            
            pdf_full = os.path.join(data_dir, pdf_rel)
            rcp_full = os.path.join(data_dir, rcp_rel)

            # [1단계: 읽기] 실제 PDF 바이너리 파싱 & JPG 이미지 검사
            pdf_data = extract_invoice_data_from_pdf(pdf_full)
            rcp_info = inspect_receipt_photo(rcp_full)
            
            if "기울기" in rcp_info["orientation"] or "수직" in rcp_info["orientation"]:
                tilted_scans_count += 1
                scan_log = f"{rcp_info['orientation']} [{rcp_info['distance']}, 해상도 {rcp_info['size'][0]}x{rcp_info['size'][1]}] -> 실무자 화면 회전 후 검수 직인 판독"
            else:
                scan_log = f"{rcp_info['orientation']} [{rcp_info['distance']}, 해상도 {rcp_info['size'][0]}x{rcp_info['size'][1]}] -> 검수 직인 정상 확인"

            print(f"\n--- [청구 건 {total_count:02d}] {inv_no} 바이너리 서류 열람 및 대조 ---")
            print(f" [읽기] PDF 청구서 판독 ({os.path.basename(pdf_rel)}): 운송사={carrier}, 차량={pdf_data['vehicle_no']}, 청구액={pdf_data['total_claim']:,}원")
            print(f"        JPG 인수증 확인 ({os.path.basename(rcp_rel)}): {scan_log}")

            # [2단계: 나누기] 대조 항목 분리
            v_no = pdf_data["vehicle_no"]
            route = pdf_data["route"]
            claimed_base = pdf_data["claimed_base"]
            claimed_sur = pdf_data["claimed_surcharge"]
            print(f" [나누기] 대조 단위 분리: 차량번호[{v_no}] | 구간[{route}] | 기본운임[{claimed_base:,}원] | 할증[{claimed_sur:,}원 / {pdf_data['surcharge_name']}]")

            # [3단계: 찾아보기/대조] 내부 시스템 검색
            print(f" [찾아보기] 배차 일지 마스터(dispatch_lookup.csv)에서 차량번호 '{v_no}' 검색...")
            matched_dsp = dispatch_map.get(v_no)

            # [4단계: 초안 작성 및 판정]
            if not matched_dsp:
                rework_count += 1
                reason = "배차 일지 상 차량 운행 기록 누락 (미승인 운행)"
                print(f" [초안] [!] 불일치 발생: {reason} -> 당일 지급 승인 보류 전표 작성")
                continue

            appr_base = int(matched_dsp["approved_freight"])
            appr_sur = int(matched_dsp["approved_surcharge"])
            appr_route = matched_dsp["route"]

            if claimed_base != appr_base:
                rework_count += 1
                reason = f"기본 운임 불일치 (청구: {claimed_base:,}원 vs 승인: {appr_base:,}원)"
                print(f" [초안] [!] 불일치 발생: {reason} -> 지급 보류 및 정위치 재청구 공문 초안 작성")
            elif claimed_sur != appr_sur:
                rework_count += 1
                reason = f"할증료 불일치 (청구: {claimed_sur:,}원 vs 승인: {appr_sur:,}원)"
                print(f" [초안] [!] 불일치 발생: {reason} -> 현장 인수증 재확인 및 과청구 소명 요구서 작성")
            elif route != appr_route:
                rework_count += 1
                reason = f"운행 구간 불일치 (청구: {route} vs 승인: {appr_route})"
                print(f" [초안] [!] 불일치 발생: {reason} -> 배차팀 오배송 확인 요청서 작성")
            else:
                matched_count += 1
                print(f" [초안] [v] 일치 확인: 청구운임 {appr_base + appr_sur:,}원 배차내역과 부합 -> 전표 승인 완료")

    # 결과 요약 및 인건비 분석
    hourly_wage = 25000
    handling_min = 12
    rework_min = 10

    total_work_minutes = (total_count * handling_min) + (rework_count * rework_min)
    total_labor_cost = (total_work_minutes / 60) * hourly_wage
    daily_rework_cost = (rework_count * rework_min / 60) * hourly_wage

    print("\n" + "=" * 85)
    print(" [바이너리 서류 대조 결과 요약 및 인건비 분석]")
    print("=" * 85)
    print(f" - 총 검토 건수      : {total_count}건 (PDF 청구서 40장 + JPG 현장 인수증 40장)")
    print(f" - 현장 촬영 노이즈  : 회전/기울기/원거리 인수증 {tilted_scans_count}건 판독 완료")
    print(f" - 정상 매칭(승인)   : {matched_count}건")
    print(f" - 지급 보류(재작업) : {rework_count}건 (재작업률: {rework_count / total_count * 100:.1f}%)")
    print(f" - 일 총 소요 시간   : {total_work_minutes / 60:.2f}시간 (기본 검토: {total_count * handling_min / 60:.1f}h + 재작업: {rework_count * rework_min / 60:.2f}h)")
    print(f" - 일 총 인건비      : {int(total_labor_cost):,}원")
    print(f" - 일 재작업 손실액  : {int(daily_rework_cost):,}원 (월 환산 추정 손실: {int(daily_rework_cost * 20):,}원)")
    print("=" * 85)

if __name__ == "__main__":
    run_simulation()
