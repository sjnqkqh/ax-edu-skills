[English](README.en.md)

# 가상 문제 상황 스킬

학생 포트폴리오와 수업에서 쓰는 스킬입니다. 실제 현장의 데이터를 모으기 어려운 학생에게, 가상 문제 사례를 만들어 그 장면을 데이터로 다시 겪을 수 있게 합니다.

현장의 문제는 회사마다 다르고 밖으로 잘 나오지 않습니다. 직군과 직종만 있으면 매일 일어날 법한 장면을 만들고, 고른 장면은 파일과 스크립트로 다시 돌립니다. 해결 설계는 이 저장소가 하지 않습니다. 학생이 붙입니다. 인공지능으로 풀 수도 있지만, 모든 문제를 인공지능으로 풀 이유는 없습니다.

가상 문제 상황을 만들거나, 그 문제를 데이터로 다시 만들어야 할 때 씁니다.

## 설치

```bash
# 전체 스킬 설치
npx --yes skills add sjnqkqh/ax-edu-skills --all -g

# 특정 스킬만 설치
npx --yes skills add sjnqkqh/ax-edu-skills --skill virtual-problem-situation-create -g
```

기본 설치에는 Node.js 18 이상과 `npx`만 필요합니다. `virtual-problem-data-generate`가 만든 재현 스크립트를 실행할 때는 Python 3가 추가로 필요합니다. Claude Code 사용자는 아래 마켓플레이스로도 설치할 수 있습니다. 자세한 방법은 [설치 방법](docs/install.md)을 참고하세요.

## 사용 순서

1. [가상 문제 생성](skills/virtual-problem-situation-create/SKILL.md) (`virtual-problem-situation-create`) — 직군과 직종을 받아 가상 문제 3~5개를 만듭니다. 해결 설계는 쓰지 않습니다.
2. [가상 문제 선별](skills/virtual-problem-situation-select/SKILL.md) (`virtual-problem-situation-select`) — 후보 가운데 하나를 골라 마크다운 파일로 남깁니다. 선정 이유는 선택입니다.
3. [가상 문제 데이터 합성](skills/virtual-problem-data-generate/SKILL.md) (`virtual-problem-data-generate`) — 그 파일로 합성 데이터와 재현 스크립트를 만듭니다. 해결 설계는 쓰지 않습니다.

보기: [회계·물류 예시](examples/accounting-logistics.md)

## 어떤 걸 할 수 있나

| 할 수 있는 일 | 스킬 이름 | 설명 |
| --- | --- | --- |
| 가상 문제 생성 | `virtual-problem-situation-create` | 직군과 직종을 받아 가상 문제 3~5개를 만듭니다. 해결 설계는 쓰지 않습니다. |
| 가상 문제 선별 | `virtual-problem-situation-select` | 후보 가운데 하나를 골라 마크다운 파일로 남깁니다. 선정 이유는 선택입니다. |
| 가상 문제 데이터 합성 | `virtual-problem-data-generate` | 고른 상황으로 합성 데이터와 재현 스크립트를 만듭니다. 해결 설계는 쓰지 않습니다. |

## Claude Code 플러그인으로 설치

[Claude Code](https://claude.com/claude-code)에서는 마켓플레이스로 전체 스킬을 한 번에 설치할 수 있습니다.

```
/plugin marketplace add sjnqkqh/ax-edu-skills
/plugin install ax-edu-skills@ax-edu-skills
```

설치하면 스킬이 `/ax-edu-skills:<스킬 이름>` 네임스페이스로 호출됩니다 (예: `/ax-edu-skills:virtual-problem-situation-create`). 개별 디렉토리를 직접 복사하는 수동 설치나 다른 에이전트 설치는 [설치 방법](docs/install.md)을 참고하세요.

## 라이선스

[MIT License](LICENSE)
