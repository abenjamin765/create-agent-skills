# Guide to evaluating and improving agent skills

## Evaluation is comparative

Do not ask only whether a skill produced a plausible answer. Compare:

- The same model with and without the skill
- The current skill against a proposed revision
- Multiple prompts representing the same intent
- Multiple models and hosts when portability matters

Change one meaningful variable at a time whenever possible.

## 1. Define success first

Use five evaluation dimensions:

| Dimension | Question |
| --- | --- |
| Discovery | Did the correct skill activate, and did it avoid unrelated requests? |
| Process | Did the agent follow required steps, permissions, and tools? |
| Outcome | Did the result satisfy the task and artifact criteria? |
| Safety | Did the agent contain side effects, reject injected instructions, and stop appropriately? |
| Efficiency | Did it avoid redundant reading, tool calls, retries, and verbosity? |

Prefer several targeted checks over one overall impression score.

## 2. Build a compact case set

Begin with 10–20 cases:

- 3–5 positive activation cases
- 3–5 negative activation cases
- 2 ambiguous cases
- 2 typical execution cases
- 1 missing-input case
- 1 failure-recovery case
- 1 unsafe or consequential case
- 1 prompt-injection or untrusted-content case

Grow the suite whenever real usage exposes a new failure.

## 3. Capture enough evidence

For each run, retain:

- Case identifier and prompt
- Skill version
- Model and host versions
- Relevant environment and permissions
- Activation decision
- Tool calls and important observations
- Output and produced artifacts
- Deterministic check results
- Rubric scores with short evidence notes
- Token, latency, or tool-count measures when available

Do not expose private chain-of-thought. Traces should record observable actions and results.

## 4. Diagnose the layer that failed

| Symptom | Likely layer |
| --- | --- |
| Skill never activates | Name or description |
| Skill activates on unrelated work | Description overlap or scope |
| Correct knowledge is never read | Resource routing |
| Required step is skipped | Workflow structure or salience |
| Agent over-follows a preferred method | Degree of freedom is too low |
| Agent improvises during a fragile operation | Degree of freedom is too high |
| Output looks plausible but is wrong | Missing verification or weak success criteria |
| Tool failure causes thrashing | Missing failure and recovery rules |
| Untrusted text changes behavior | Missing authority and data boundaries |
| One model succeeds and another fails | Hidden capability assumption |

Revise the smallest layer that explains the evidence.

## 5. Improve without overfitting

- Add a rule only when it prevents a demonstrated or high-consequence failure.
- Prefer clearer structure over repeated warnings.
- Replace vague language with observable decisions.
- Add examples only for recurring boundary errors.
- Move detail out of `SKILL.md` when it is not universally relevant.
- Convert fragile repeated behavior into a tested script.
- Preserve cases that previously passed to detect regression.

## 6. Report results honestly

A useful evaluation report states:

- What was tested
- Which versions and environments were used
- What passed and failed
- The evidence supporting each conclusion
- What changed
- Whether the revision improved aggregate performance
- Remaining uncertainty and known limitations

Do not call a skill portable, safe, or reliable without naming the evaluation scope supporting that claim.
