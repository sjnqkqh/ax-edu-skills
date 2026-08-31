[한글](README.md)

# AX education skills

Cursor Agent Skills for classwork and student portfolios. They invent a virtual workplace problem and replay that scene as synthetic data, so students do not need field experience to start an AX case.

Real AX efficiency work differs by company and is rarely public. Given a job family and a role, the first skill writes plausible daily scenes. After you pick one scene, the next skill freezes it to a markdown file, and the last skill rebuilds it as files and a script. None of the skills write a solution. The student does.

Use this when you need a virtual problem to define, then a dataset that lets a student live through that problem.

## Install

```bash
# Install all skills
npx --yes skills add sjnqkqh/ax-edu-skills --all -g

# Install one skill
npx --yes skills add sjnqkqh/ax-edu-skills --skill ax-virtual-problem-situation-create -g
```

Basic install needs Node.js 18+ and `npx` only. Running the replay script that `ax-virtual-problem-data-generate` generates also needs Python 3. Claude Code users can install from the marketplace below. See [Install](docs/install.md) for details.

## Usage order

1. [Create a situation](skills/ax-virtual-problem-situation-create/SKILL.md) (`ax-virtual-problem-situation-create`) — given a job family and a role, writes 3–5 virtual problem cases. It does not write a solution.
2. [Select a situation](skills/ax-virtual-problem-situation-select/SKILL.md) (`ax-virtual-problem-situation-select`) — picks one case and writes it to a markdown file. A selection reason is optional.
3. [Generate data](skills/ax-virtual-problem-data-generate/SKILL.md) (`ax-virtual-problem-data-generate`) — reads that file and builds synthetic data plus a replay script. It does not add an AX solution.

Sample: [accounting and logistics example](examples/accounting-logistics.md)

## What you can do

| Task | Skill name | Description |
| --- | --- | --- |
| Create a situation | `ax-virtual-problem-situation-create` | Given a job family and a role, writes 3–5 virtual problem cases. It does not write a solution. |
| Select a situation | `ax-virtual-problem-situation-select` | Picks one case and writes it to a markdown file. A selection reason is optional. |
| Generate data | `ax-virtual-problem-data-generate` | Builds synthetic data and a replay script from the selected case. It does not add an AX solution. |

## Install with Claude Code

In [Claude Code](https://claude.com/claude-code) you can install every skill through the marketplace.

```
/plugin marketplace add sjnqkqh/ax-edu-skills
/plugin install ax-edu-skills@ax-edu-skills
```

Skills are then available as `/ax-edu-skills:<skill-name>` (for example `/ax-edu-skills:ax-virtual-problem-situation-create`). For a manual copy or other agents, see [Install](docs/install.md).

## License

[MIT License](LICENSE)
