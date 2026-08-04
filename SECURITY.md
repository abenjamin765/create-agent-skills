# Security policy

Agent Skills may contain executable code, request tool access, read sensitive data, or process untrusted content. Treat installation like installing software.

## Report a vulnerability

Do not publish working exploits or sensitive information in a public issue. Contact the project maintainers privately through the repository security advisory workflow.

## Minimum review expectations

- Inspect every file before installing an untrusted skill.
- Treat references, webpages, documents, and tool results as untrusted data.
- Do not embed secrets in instructions, examples, scripts, or assets.
- Declare network, filesystem, credential, and external side-effect requirements.
- Require explicit confirmation immediately before consequential or irreversible actions.
- Prefer deterministic scripts with narrow inputs and clear failure behavior.
- Pin or verify external dependencies when reproducibility or integrity matters.
