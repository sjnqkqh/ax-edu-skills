[한글](README.md)

# AX education skills

Cursor Agent Skills for classwork and student portfolios. They invent a virtual workplace problem and replay that scene as synthetic data, so students do not need field experience to start an AX case.

Real AX efficiency work differs by company and is rarely public. Given a job family and a role, the first skill writes plausible daily scenes. After you pick one scene, the next skill freezes it to a markdown file, and the last skill rebuilds it as files and a script. None of the skills write a solution. The student does.

Use this when you need a virtual problem to define, then a dataset that lets a student live through that problem.

## Install

```bash
# Install all skills
npx --yes skills add sjnqkqh/ax-edu-skills --skill '*' -g -y --agent aider-desk amp antigravity antigravity-cli astrbot autohand-code augment bob claude-code openclaw cline codearts-agent codebuddy codemaker codestudio codex command-code continue cortex crush cursor deepagents devin dexto droid firebender forgecode gemini-cli github-copilot goose grok hermes-agent inference-sh jazz junie iflow-cli kilo kimchi kimi-code-cli kiro-cli kode lingma loaf mcpjam minimax-code mistral-vibe moxby mux opencode openhands ona pi posit-assistant qoder qoder-cn qwen-code replit reasonix rovodev roo tabnine-cli terramind tinycloud trae trae-cn warp windsurf zed zcode zencoder zenflow neovate pochi adal universal

# Install one skill
npx --yes skills add sjnqkqh/ax-edu-skills --skill ax-virtual-problem -g -y --agent aider-desk amp antigravity antigravity-cli astrbot autohand-code augment bob claude-code openclaw cline codearts-agent codebuddy codemaker codestudio codex command-code continue cortex crush cursor deepagents devin dexto droid firebender forgecode gemini-cli github-copilot goose grok hermes-agent inference-sh jazz junie iflow-cli kilo kimchi kimi-code-cli kiro-cli kode lingma loaf mcpjam minimax-code mistral-vibe moxby mux opencode openhands ona pi posit-assistant qoder qoder-cn qwen-code replit reasonix rovodev roo tabnine-cli terramind tinycloud trae trae-cn warp windsurf zed zcode zencoder zenflow neovate pochi adal universal
```

Basic install needs Node.js 18+ and `npx` only. Running the `replay.py` that `ax-synthetic-replay` generates also needs Python 3. Claude Code users can install from the marketplace below. See [Install](docs/install.md) for details.

## Usage order

1. [AX Virtual Problem](skills/ax-virtual-problem/SKILL.md) (`ax-virtual-problem`) — given a job family and a role, writes 3–5 virtual problem cases. It does not write a solution.
2. [AX Virtual Problem Select](skills/ax-virtual-problem-select/SKILL.md) (`ax-virtual-problem-select`) — picks one case and writes it to a markdown file. A selection reason is optional.
3. [AX Synthetic Replay](skills/ax-synthetic-replay/SKILL.md) (`ax-synthetic-replay`) — reads that file and builds synthetic data plus a Python replay script. It does not add an AX solution.

Sample: [accounting and logistics example](examples/accounting-logistics.md)

## What you can do

| Task | Skill name | Description |
| --- | --- | --- |
| Invent virtual problem cases | `ax-virtual-problem` | Given a job family and a role, writes 3–5 virtual problem cases. It does not write a solution. |
| Freeze one case | `ax-virtual-problem-select` | Picks one case and writes it to a markdown file. A selection reason is optional. |
| Replay the scene as data | `ax-synthetic-replay` | Builds synthetic data and a Python replay script from the selected case. It does not add an AX solution. |

## Install with Claude Code

In [Claude Code](https://claude.com/claude-code) you can install every skill through the marketplace.

```
/plugin marketplace add sjnqkqh/ax-edu-skills
/plugin install ax-edu-skills@ax-edu-skills
```

Skills are then available as `/ax-edu-skills:<skill-name>` (for example `/ax-edu-skills:ax-virtual-problem`). For a manual copy or other agents, see [Install](docs/install.md).

## License

[MIT License](LICENSE)
