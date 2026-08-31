[English](README.en.md)

# AX education skills

학생 포트폴리오와 수업에서 쓰는 Cursor Agent Skill입니다. 현장 전문가가 아니어도, 가상 문제 상황을 만들고 그 장면을 합성 데이터로 다시 겪을 수 있게 합니다.

현장의 AX 효율화 문제는 회사마다 다르고 밖으로 잘 나오지 않습니다. 직군과 직종만 있으면 매일 일어날 법한 장면을 만들고, 고른 장면은 파일과 스크립트로 다시 돌립니다. 해결 설계는 이 저장소가 하지 않습니다. 학생이 붙입니다.

가상 현장을 만들어 문제를 정의하거나, 그 문제를 데이터로 재현해야 할 때 씁니다.

## 설치

```bash
# 전체 스킬 설치
npx --yes skills add sjnqkqh/ax-edu-skills --skill '*' -g -y

# 특정 스킬만 설치
npx --yes skills add sjnqkqh/ax-edu-skills --skill ax-virtual-problem -g -y
```

기본 설치에는 Node.js 18 이상과 `npx`만 필요합니다. `ax-synthetic-replay`가 만든 `replay.py`를 실행할 때는 Python 3가 추가로 필요합니다. Claude Code 사용자는 아래 마켓플레이스로도 설치할 수 있습니다. 자세한 방법은 [설치 방법](docs/install.md)을 참고하세요.

## 사용 순서

1. [AX Virtual Problem](skills/ax-virtual-problem/SKILL.md) (`ax-virtual-problem`) — 직군과 직종을 받아 가상 문제 상황 3~5개를 만듭니다. 해결 설계는 쓰지 않습니다.
2. [AX Virtual Problem Select](skills/ax-virtual-problem-select/SKILL.md) (`ax-virtual-problem-select`) — 후보 가운데 하나를 골라 마크다운 파일로 남깁니다. 선정 이유는 선택입니다.
3. [AX Synthetic Replay](skills/ax-synthetic-replay/SKILL.md) (`ax-synthetic-replay`) — 그 파일로 합성 데이터와 Python 재현 스크립트를 만듭니다. AX 해결책은 넣지 않습니다.

보기: [회계·물류 예시](examples/accounting-logistics.md)

## 어떤 걸 할 수 있나

| 할 수 있는 일 | 스킬 이름 | 설명 |
| --- | --- | --- |
| 가상 문제 상황 만들기 | `ax-virtual-problem` | 직군과 직종을 받아 가상 문제 상황 3~5개를 만듭니다. 해결 설계는 쓰지 않습니다. |
| 가상 문제 상황 고르기 | `ax-virtual-problem-select` | 후보 가운데 하나를 골라 마크다운 파일로 남깁니다. 선정 이유는 선택입니다. |
| 합성 데이터로 장면 재현 | `ax-synthetic-replay` | 고른 상황으로 합성 데이터와 Python 재현 스크립트를 만듭니다. AX 해결책은 넣지 않습니다. |

## Claude Code 플러그인으로 설치

[Claude Code](https://claude.com/claude-code)에서는 마켓플레이스로 전체 스킬을 한 번에 설치할 수 있습니다.

```
/plugin marketplace add sjnqkqh/ax-edu-skills
/plugin install ax-edu-skills@ax-edu-skills
```

설치하면 스킬이 `/ax-edu-skills:<스킬 이름>` 네임스페이스로 호출됩니다 (예: `/ax-edu-skills:ax-virtual-problem`). 개별 디렉토리를 직접 복사하는 수동 설치나 다른 에이전트 설치는 [설치 방법](docs/install.md)을 참고하세요.

## 라이선스

[MIT License](LICENSE)
