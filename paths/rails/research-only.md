# Research-only scope rails (HARD limits)

> This file is inlined into every `research_only` worker task. The approved
> outcome is a decision-ready research artifact, not implementation.

## Allowed work

- Read the item, approved proposal, provided project materials, and public or
  otherwise already-authorized sources.
- Analyze requirements, technical options, risks, dependencies, and trade-offs.
- Produce research notes, architecture recommendations, plans, and decision
  records in the pipeline-managed persistent workspace.

## Never allowed

- Do not implement or modify project code.
- Do not deploy, publish, modify production systems, or perform external side
  effects.
- Do not access, disclose, copy, log, transmit, or commit credentials, tokens,
  keys, secrets, or private configuration.
- Do not modify Hermes configuration, profiles, skills, cron jobs, gateways, or
  other Hermes runtime settings.
- Do not modify an unrelated repository or work in arbitrary external
  repositories in V1.

## If research reveals implementation work

Document the recommended scope and request a separate approved software-project
proposal. Do not begin implementation in this path.
