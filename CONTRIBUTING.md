# Contributing

Portable Agent Skills is developed as an evidence-seeking standard. Proposals should distinguish interoperability requirements from authoring recommendations and untested hypotheses.

## Propose a change

1. Describe the failure or opportunity using a concrete task.
2. Include the affected model, host, skill version, and environment.
3. Provide the prompt, relevant trace, output, and validator results when possible.
4. Explain whether the proposal changes the portable format, authoring guidance, or evaluation method.
5. Add or update evaluation cases that would detect the behavior.

## Normative language

Use **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** as defined by RFC 2119 only in normative specification text. Use ordinary language in guides and examples.

## Validate changes

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

## Evidence levels

Label significant guidance with the strongest available evidence:

- **Interoperability** — required by one or more host implementations.
- **Observed** — supported by reproducible model or host evaluations.
- **Transferred** — adapted from another discipline and awaiting direct validation.
- **Hypothesis** — plausible but not yet evaluated.
