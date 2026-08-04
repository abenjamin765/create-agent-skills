# Portable authoring standard

## Contents

- Behavioral contract
- Discovery
- Instruction language
- Progressive disclosure
- Examples
- Verification
- Evaluation minimum

## Behavioral contract

Define the expected inputs, preconditions, outcome, invariants, postconditions, side effects, failures, and recovery behavior before drafting instructions.

## Discovery

Write descriptions as routing interfaces. State the capability, likely trigger vocabulary, relevant objects or formats, and important exclusions. Test positive, negative, and ambiguous prompts.

## Instruction language

Use imperative sentences, consistent terminology, and conditions placed before governed actions. Prefer one obligation per sentence. Replace adjectives such as “good,” “polished,” or “appropriate” with observable criteria.

## Progressive disclosure

Keep the universal operational map in `SKILL.md`. Put conditional knowledge in `references/`, deterministic operations in `scripts/`, output materials in `assets/`, behavioral cases in `evals/`, and host-only extensions in `adapters/`. Avoid deep reference chains.

## Examples

Use examples to demonstrate boundaries, edge cases, exceptions, and required structures. Do not spend context demonstrating universally competent behavior.

## Verification

Define completion before execution. Prefer deterministic validators. When judgment is unavoidable, use a short rubric with observable anchors and evidence notes.

## Evaluation minimum

Include positive, negative, ambiguous, typical execution, missing input, failure recovery, consequential action, and untrusted-content cases. Record the model, host, versions, environment, observable trace, output, checks, and scores.
