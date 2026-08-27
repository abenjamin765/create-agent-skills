# Portable Agent Skills

Portable Agent Skills is an evidence-informed standard and toolkit for writing agent skills that remain understandable, testable, and useful across AI models and agent hosts.

The project extends the open [Agent Skills](https://agentskills.io/) directory format rather than replacing it. It separates three concerns:

1. **Portable specification** — the common contract hosts and tools can interpret.
2. **Authoring guidance** — practical guidance for writing effective instructions.
3. **Conformance evaluation** — evidence that a skill triggers, executes, verifies, and fails safely.

## Start here

- [Write a skill](docs/writing-skills.md)
- [Evaluate and improve a skill](docs/evaluating-skills.md)
- [Read the draft standard](docs/standard.md)
- [Review the research foundations](docs/research-foundations.md)

## Installable skills

This repository includes two portable Agent Skills:

- [`create-agent-skill`](skills/create-agent-skill/SKILL.md) turns representative tasks into a focused, portable skill package.
- [`evaluate-agent-skill`](skills/evaluate-agent-skill/SKILL.md) evaluates discovery, execution, outcomes, safety, efficiency, and portability, then proposes evidence-backed improvements.

Install them using any Agent Skills-compatible host or installer. For a manual installation, copy the desired skill directory into one of the skill locations supported by your host, commonly `.agents/skills/` for a project or `~/.agents/skills/` for a user.

```bash
mkdir -p .agents/skills
cp -R skills/create-agent-skill .agents/skills/
cp -R skills/evaluate-agent-skill .agents/skills/
```

## Repository structure

```text
portable-agent-skills/
├── docs/                   Standard, guides, and research rationale
├── schema/                 Machine-readable extension schemas
├── skills/                 Installable agent skills
├── examples/               Conforming example packages
├── evals/                  Reusable evaluation cases and schemas
├── scripts/                Deterministic validators
└── .github/workflows/      Continuous validation
```

## Design principles

- Treat a skill as a behavioral contract, not a long prompt.
- Design backward from observable outcomes.
- Treat discovery as a classification problem.
- Establish inputs, assumptions, authority, and stop conditions.
- Match instruction specificity to task risk and variability.
- Use progressive disclosure along meaningful decision boundaries.
- Write in concise, controlled, cooperative language.
- Demonstrate only non-obvious decisions and edge cases.
- Close the loop with explicit verification and recovery.
- Declare capabilities, side effects, and confirmation gates.
- Design for composition and graceful degradation.
- Require cross-model evidence before claiming portability.

## Project status

This is an early draft intended for experimentation and public review. The initial goal is to develop a useful authoring profile and evaluation methodology while remaining compatible with the existing Agent Skills format.

## Related projects

- [Many Hats](https://github.com/abenjamin765/many-hats) — a cloneable AI product team whose portable skills follow this contract

## License

MIT License. See [LICENSE](LICENSE).
