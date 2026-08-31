# 설치 방법

## 기본 설치 흐름

1. Node.js 18 이상과 `npx`가 사용 가능한지 확인합니다.
2. 합성 데이터 재현 결과를 `python replay.py`로 돌릴 때는 Python 3가 사용 가능한지 확인합니다.
3. 전체 스킬을 먼저 설치합니다.
4. 그 다음 사용 순서대로 스킬을 호출합니다.

## 에이전트에게 맡기기

Codex나 Claude Code에 아래 문장을 그대로 붙여 넣으면 됩니다.

```text
이 레포의 설치 문서를 읽고 ax-edu-skills 전체 스킬을 먼저 설치해줘. 끝나면 설치된 스킬과 사용 순서만 짧게 정리해.
```

## 직접 설치

`skills` 설치 명령은 아래 셋 중 하나만 있으면 됩니다.

```bash
npx --yes skills add sjnqkqh/ax-edu-skills --list
pnpm dlx skills add sjnqkqh/ax-edu-skills --list
bunx skills add sjnqkqh/ax-edu-skills --list
```

권장: 전체 스킬 먼저 설치

```bash
npx --yes skills add sjnqkqh/ax-edu-skills --all -g
```

특정 스킬만 설치

```bash
npx --yes skills add sjnqkqh/ax-edu-skills --skill ax-virtual-problem -g
npx --yes skills add sjnqkqh/ax-edu-skills --skill ax-virtual-problem-select -g
npx --yes skills add sjnqkqh/ax-edu-skills --skill ax-synthetic-replay -g
```

설치 반영 확인

```bash
npx --yes skills ls -g
```

로컬 저장소에서 바로 전체 설치 테스트

```bash
npx --yes skills add . --all -g
```

## 전역 설치에서 Eve, PromptScript

`--all -g`는 전역 설치를 지원하는 에이전트에 세 스킬을 넣습니다. Eve와 PromptScript는 프로젝트 전용이라 전역 설치를 지원하지 않습니다. 그 두 곳에 실패가 찍혀도 나머지 에이전트에는 설치됩니다. 이 저장소의 스킬을 고쳐도 없어지지 않으며, `skills` CLI 쪽 제한입니다.

그 둘에 넣으려면 `-g` 없이 프로젝트 설치를 씁니다.

```bash
npx --yes skills add sjnqkqh/ax-edu-skills --all
```

## Claude Code 플러그인으로 설치

```
/plugin marketplace add sjnqkqh/ax-edu-skills
/plugin install ax-edu-skills@ax-edu-skills
```

## npx도 없으면

`npx`, `pnpm dlx`, `bunx` 중 아무것도 없으면 먼저 Node.js 계열 런타임을 설치해야 합니다.

- `npx`를 쓰려면 Node.js + npm
- `pnpm dlx`를 쓰려면 pnpm
- `bunx`를 쓰려면 Bun

## 수동 복사

`npx`를 쓰지 않을 때만 아래 폴더를 프로젝트의 `.cursor/skills/` 또는 사용자 스킬 폴더로 복사합니다.

- `skills/ax-virtual-problem`
- `skills/ax-virtual-problem-select`
- `skills/ax-synthetic-replay`

이 저장소를 프로젝트 루트로 열면 `.cursor/skills/`에 같은 스킬이 이미 있습니다.

## 합성 데이터 재현을 돌릴 때

`ax-synthetic-replay`가 만든 `replay.py`는 Python 3 표준 라이브러리만 씁니다. 스킬 설치와는 별개이며, 재현 스크립트를 실행할 때만 Python 3가 필요합니다.
