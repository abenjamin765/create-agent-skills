# Guide to writing portable agent skills

## 1. Start with tasks, not prose

Collect five to ten representative requests before writing the skill:

- Clear requests that should activate it
- Neighboring requests that should not
- Ambiguous requests requiring a decision
- At least one edge case
- At least one unsafe or impossible case

For each request, define the observable result and the mistakes that would make the result unacceptable.

## 2. Define the behavioral contract

Write down:

- **Outcome:** What changes or is produced?
- **Inputs:** What must be supplied or discovered?
- **Preconditions:** What must be true before acting?
- **Invariants:** What must remain true throughout?
- **Postconditions:** How can completion be verified?
- **Side effects:** What external state may change?
- **Failures:** When must the agent retry, ask, degrade, or stop?

If these cannot be stated clearly, the skill is not yet ready to write.

## 3. Write the description as a router

The description is the only information many hosts see before activation. Begin with the capability, then specify the trigger context and important neighboring boundaries.

Weak:

```yaml
description: Helps with documentation.
```

Stronger:

```yaml
description: Creates and revises API reference documentation from source code and schemas. Use for endpoint references, parameter tables, request and response examples, and API documentation audits; do not use for general product copy or tutorials.
```

Evaluate descriptions like classifiers rather than judging whether they sound polished.

## 4. Choose the right degree of freedom

| Situation | Instruction style |
| --- | --- |
| Many valid approaches; context determines quality | State goals, heuristics, and tradeoffs. |
| A preferred pattern allows controlled variation | Provide pseudocode, templates, or parameterized scripts. |
| Errors are dangerous, expensive, or difficult to reverse | Provide exact sequences, confirmation gates, and deterministic validators. |

Only constrain decisions that matter. A long sequence of unnecessary rules makes the skill brittle and can hide the critical ones.

## 5. Build an operational map

A useful default structure is:

```markdown
# Outcome

# Required inputs

# Workflow
1. Inspect...
2. Choose...
3. Execute...
4. Verify...

# Decision rules

# Safety and permissions

# Output contract

# Failure and recovery

# Resources
```

Adapt the structure to the task. Do not add empty or redundant sections merely to follow the template.

## 6. Route supporting material deliberately

- Put core decisions and sequence in `SKILL.md`.
- Put detailed, conditional knowledge in `references/`.
- Put repeated deterministic operations in `scripts/`.
- Put templates and output materials in `assets/`.
- Put host-only additions in `adapters/`.
- Put reproducible behavioral cases in `evals/`.

Reference each conditional file directly from `SKILL.md` and explain when to use it.

## 7. Use controlled language

- Write imperatively: “Inspect the repository state.”
- Put conditions first: “If the worktree contains unrelated changes, ask which files belong.”
- Give one instruction per sentence.
- Use the same term for the same object.
- Replace “high quality” with observable criteria.
- Avoid pronouns when their referent could be unclear.
- Reserve uppercase normative keywords for genuine requirements.

## 8. Use examples strategically

Include an example when it teaches a boundary or decision the instructions do not make sufficiently concrete. Prefer paired examples when distinguishing neighboring cases.

Do not include examples merely to restate obvious steps. Examples consume context and may accidentally narrow behavior.

## 9. Close the loop

Define completion before execution. Prefer deterministic checks such as schemas, linters, parsers, test commands, renderers, and file assertions. When judgment is necessary, use a short rubric with observable anchors.

Use the pattern:

1. Produce or change the artifact.
2. Run the relevant checks.
3. Diagnose specific failures.
4. Revise only what the failures justify.
5. Repeat until the checks pass or a declared stop condition occurs.

## 10. Test before claiming portability

Evaluate at least:

- Positive, negative, and ambiguous activation prompts
- A typical happy path
- Missing required input
- An edge case
- A tool or dependency failure
- An unsafe or destructive request
- An indirect-instruction or untrusted-content case
- A smaller and a larger model
- Every host named in the compatibility claim

Record the environment and model versions. Portability is an empirical claim, not a formatting property.
