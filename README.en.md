[한글](README.md)

# AX education skills

Cursor Agent Skills for classwork and student portfolios. They invent a virtual workplace problem and replay that scene as synthetic data, so students do not need field experience to start an AX case.

Real AX efficiency work differs by company and is rarely public. Given a job family and a role, the first skill writes plausible daily scenes. After you pick one scene, the next skill freezes it to a markdown file, and the last skill rebuilds it as files and a script. None of the skills write a solution. The student does.

Use this when you need a virtual problem to define, then a dataset that lets a student live through that problem.

## Usage order

1. [AX Virtual Problem](skills/ax-virtual-problem/SKILL.md) — given a job family and a role, writes 3–5 virtual problem cases. It does not write a solution.
2. [AX Virtual Problem Select](skills/ax-virtual-problem-select/SKILL.md) — picks one case and writes it to a markdown file. A selection reason is optional.
3. [AX Synthetic Replay](skills/ax-synthetic-replay/SKILL.md) — reads that file and builds synthetic data plus a Python replay script. It does not add an AX solution.

Sample: [accounting and logistics example](examples/accounting-logistics.md)

## Install

Clone this repository, then copy these folders into the project's `.cursor/skills/` directory or into your user skills directory.

- `skills/ax-virtual-problem`
- `skills/ax-virtual-problem-select`
- `skills/ax-synthetic-replay`

If you open this repository as the project root, the same skills are already under `.cursor/skills/`. Invoke them by name in chat.

## License

[MIT License](LICENSE)
