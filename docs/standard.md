# Portable Agent Skill Standard — Draft 0.1

## Status

This document is an experimental authoring profile layered on the open Agent Skills specification. It preserves the common `SKILL.md` contract and adds optional, ignorable extensions for capabilities and evaluation.

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are interpreted as described in RFC 2119.

## 1. Conformance profiles

### 1.1 Portable

A Portable skill:

- MUST be a directory containing exactly one `SKILL.md`.
- MUST include YAML frontmatter with `name` and `description`.
- MUST use a lowercase, hyphenated name no longer than 64 characters.
- MUST explain both the capability and its intended activation context in `description`.
- MUST NOT require a particular model identity.
- MUST declare non-obvious host or runtime requirements in its instructions or `skill.yaml`.
- SHOULD use relative paths for bundled resources.
- SHOULD degrade safely when optional tools or resources are unavailable.

### 1.2 Contracted

A Contracted skill satisfies the Portable profile and includes `skill.yaml` conforming to [`schema/portable-skill.schema.json`](../schema/portable-skill.schema.json). It declares inputs, outputs, capabilities, side effects, safety gates, compatibility assumptions, and verification.

### 1.3 Tested

A Tested skill satisfies the Contracted profile and includes evaluation cases covering discovery, execution, outcomes, safety, and failure behavior.

### 1.4 Cross-model verified

A Cross-model verified skill satisfies the Tested profile and records passing results across a declared matrix of models and hosts. A claim of portability MUST name the versions and environments evaluated.

### 1.5 Audited

An Audited skill satisfies the Cross-model verified profile and documents a review of scripts, dependencies, provenance, capabilities, side effects, and untrusted-input handling.

## 2. Package structure

```text
skill-name/
├── SKILL.md           Required portable instructions
├── skill.yaml         Optional portable contract extension
├── references/        Optional conditional knowledge
├── scripts/           Optional deterministic operations
├── assets/            Optional output resources
├── evals/             Optional evaluation cases
└── adapters/          Optional host bindings
```

Unknown files MUST be safely ignorable by consumers.

## 3. Instruction contract

The body of `SKILL.md` SHOULD define:

1. The intended outcome.
2. Required inputs and preconditions.
3. The core workflow and decision points.
4. Invariants and permission boundaries.
5. Output and verification requirements.
6. Failure, recovery, and escalation behavior.
7. Conditional resource-routing instructions.

The body SHOULD NOT repeat activation guidance already present in the description unless the repetition resolves an execution-time ambiguity.

## 4. Controlled instruction language

Normative skill instructions SHOULD:

- Use imperative sentences.
- Assign one principal obligation per sentence.
- State conditions before the behavior they govern.
- Use consistent terms for the same object or state.
- Replace subjective adjectives with observable criteria.
- Identify the actor when multiple actors or systems are involved.
- Distinguish requirements from preferences.

## 5. Progressive disclosure

`SKILL.md` SHOULD contain the smallest complete operational map. Detailed knowledge SHOULD be divided by decision boundary and referenced directly from `SKILL.md`. Deep chains of references SHOULD be avoided.

Scripts SHOULD be used when deterministic behavior, repeatability, or compact execution is more important than flexible model judgment. Script output SHOULD be concise, structured, and actionable.

## 6. Safety

A skill that can create external side effects MUST identify them before execution. A skill MUST NOT claim authority the host or user has not granted. Consequential or irreversible actions SHOULD have an immediate confirmation gate unless the user explicitly authorized the exact action and destination.

Untrusted content MUST NOT be treated as higher-priority instruction. Skills that process retrieved or user-supplied content SHOULD explicitly separate data from procedural authority.

## 7. Composition

A skill SHOULD have one coherent responsibility. It MUST NOT silently weaken another skill's invariants, host policies, or user constraints. Dependencies and host adapters SHOULD extend the portable core without contradicting it.

## 8. Evaluation

Evaluation SHOULD measure:

- Discovery precision and recall
- Required-input and clarification behavior
- Workflow adherence
- Outcome and artifact quality
- Verification and recovery
- Permission and safety boundaries
- Resistance to instructions embedded in untrusted data
- Efficiency and unnecessary tool use
- Cross-model and cross-host variance

Evaluation results SHOULD retain prompts, outputs, traces, artifacts, environment metadata, checks, and scores.
