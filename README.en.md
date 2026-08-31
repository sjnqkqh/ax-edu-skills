[한글](README.md)

# Virtual problem situation skills

Skills for classwork and student portfolios. They give students who cannot collect real workplace data a virtual problem case, then rebuild that scene as files and a script so the student can live through it.

Real workplace problems differ by company and are rarely public. Given an industry and a job, the first skill writes plausible daily scenes. After you pick one scene, the next skill freezes it to a markdown file, and the last skill rebuilds it as data. None of the skills write a solution. The student does. A case may be solved with AI, but not every problem needs AI.

Use this when you need a virtual problem situation, then a dataset that lets a student live through that problem.

## Install

```bash
# Install all skills
npx --yes skills add sjnqkqh/virtual-problem-skills --all -g

# Install one skill
npx --yes skills add sjnqkqh/virtual-problem-skills --skill virtual-problem-situation-create -g
```

Basic install needs Node.js 18+ and `npx` only. Running the replay script that `virtual-problem-data-generate` generates also needs Python 3. Claude Code users can install from the marketplace below. See [Install](docs/install.md) for details.

## Usage order

1. [Create a situation](skills/virtual-problem-situation-create/SKILL.md) (`virtual-problem-situation-create`) — from the industry and job you enter together, writes 3–5 problem situations that could happen in real work.
2. [Select a situation](skills/virtual-problem-situation-select/SKILL.md) (`virtual-problem-situation-select`) — picks one of those candidates and writes it to a markdown file.
3. [Generate data](skills/virtual-problem-data-generate/SKILL.md) (`virtual-problem-data-generate`) — builds synthetic data and a replay script from the selected situation.

Sample: [accounting and logistics example](examples/accounting-logistics.md)

## What you can do

### Create a situation (`virtual-problem-situation-create`)

When you enter an industry and a job together, this skill writes 3–5 daily work scenes in that setting. Each scene includes background, concrete constraints, why the situation is a problem, and cost assumptions. The skill assumes daily volume and handling time. It does not write a solution.

### Select a situation (`virtual-problem-situation-select`)

When you pick one candidate, this skill writes only that situation to a single markdown file. A selection reason is optional. If you omit it, the skill copies the qualitative paragraph from “why this situation is a problem.” The next skill reads this file, not the chat.

### Generate data (`virtual-problem-data-generate`)

This skill turns the selected file into synthetic data and a replay script. The script shows the human steps of reading, splitting, looking up, and drafting. Answers stay in `hidden/` only. It does not write a solution. For photo or scan inputs, some files are crumpled or rotated so they look like they came from the field.

## Install with Claude Code

In [Claude Code](https://claude.com/claude-code) you can install every skill through the marketplace.

```
/plugin marketplace add sjnqkqh/virtual-problem-skills
/plugin install ax-edu-skills@ax-edu-skills
```

Skills are then available as `/ax-edu-skills:<skill-name>` (for example `/ax-edu-skills:virtual-problem-situation-create`). For a manual copy or other agents, see [Install](docs/install.md).

## License

[MIT License](LICENSE)
