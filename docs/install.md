# 설치 방법

## 기본 설치 흐름

1. Node.js 18 이상과 `npx`가 사용 가능한지 확인합니다.
2. `ax-virtual-problem-data-generate`가 만든 재현 스크립트를 돌릴 때는 Python 3가 사용 가능한지 확인합니다.
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
npx --yes skills add sjnqkqh/ax-edu-skills --skill ax-virtual-problem-situation-create -g
npx --yes skills add sjnqkqh/ax-edu-skills --skill ax-virtual-problem-situation-select -g
npx --yes skills add sjnqkqh/ax-edu-skills --skill ax-virtual-problem-data-generate -g
```

설치 반영 확인

```bash
npx --yes skills ls -g
```

로컬 저장소에서 바로 전체 설치 테스트

```bash
npx --yes skills add . --all -g
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

- `skills/ax-virtual-problem-situation-create`
- `skills/ax-virtual-problem-situation-select`
- `skills/ax-virtual-problem-data-generate`

이 저장소를 프로젝트 루트로 열면 `.cursor/skills/`에 같은 스킬이 이미 있습니다.

## 재현 스크립트를 돌릴 때

`ax-virtual-problem-data-generate`가 만든 재현 스크립트는 Python 3가 필요합니다. 패키지가 있으면 그 산출물의 README.md를 따릅니다. 스킬 설치와는 별개입니다.
