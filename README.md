[English](README.en.md)

# AX education skills

학생 포트폴리오와 수업에서 쓰는 Cursor Agent Skill입니다. 현장 전문가가 아니어도, 가상 문제 상황을 만들고 그 장면을 합성 데이터로 다시 겪을 수 있게 합니다.

현장의 AX 효율화 문제는 회사마다 다르고 밖으로 잘 나오지 않습니다. 직군과 직종만 있으면 매일 일어날 법한 장면을 만들고, 고른 장면은 파일과 스크립트로 다시 돌립니다. 해결 설계는 이 저장소가 하지 않습니다. 학생이 붙입니다.

가상 현장을 만들어 문제를 정의하거나, 그 문제를 데이터로 재현해야 할 때 씁니다.

## 사용 순서

1. [AX Virtual Problem](skills/ax-virtual-problem/SKILL.md) — 직군과 직종을 받아 가상 문제 상황 3~5개를 만듭니다. 해결 설계는 쓰지 않습니다.
2. [AX Virtual Problem Select](skills/ax-virtual-problem-select/SKILL.md) — 후보 가운데 하나를 골라 마크다운 파일로 남깁니다. 선정 이유는 선택입니다.
3. [AX Synthetic Replay](skills/ax-synthetic-replay/SKILL.md) — 그 파일로 합성 데이터와 Python 재현 스크립트를 만듭니다. AX 해결책은 넣지 않습니다.

보기: [회계·물류 예시](examples/accounting-logistics.md)

## 설치

저장소를 받은 다음, 아래 폴더를 프로젝트의 `.cursor/skills/` 또는 사용자 스킬 폴더로 복사합니다.

- `skills/ax-virtual-problem`
- `skills/ax-virtual-problem-select`
- `skills/ax-synthetic-replay`

이 저장소를 프로젝트 루트로 열면 `.cursor/skills/`에 같은 스킬이 이미 있습니다. 채팅에서 스킬 이름으로 호출하면 됩니다.

## 라이선스

[MIT License](LICENSE)
