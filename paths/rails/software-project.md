# Software project scope rails (HARD limits)

> This file is inlined into every `software_project` worker task. It is the
> safety boundary for approved website, web application, mobile application, and
> automation work. Stay within the approved proposal and this rail.

## Allowed work

- Implement the approved, bounded project inside the pipeline-managed persistent
  workspace for this item.
- Create or modify source code, tests, documentation, and local development
  configuration required by the approved scope.
- Use version control locally to inspect history, create commits, and create a
  non-protected working branch when the workspace is a Git repository.

## Never allowed

- Do not push directly to `main` or `master`.
- Do not force-push.
- Do not merge any branch without explicit human approval.
- Do not deploy, publish, release, submit to an app store, or change production
  infrastructure without explicit human approval.
- Do not modify an unrelated repository.
- Do not modify Hermes configuration, profiles, skills, cron jobs, gateways, or
  other Hermes runtime settings from a project task.
- Do not expose, copy, log, transmit, or commit credentials, tokens, keys,
  secrets, or private configuration.
- Do not create accounts, purchase services, enable billing, or add an unapproved
  third-party integration.
- Do not work in arbitrary external repositories in V1. The pipeline-managed
  persistent workspace is the implementation location.

## If the approved work does not fit

Stop and document the mismatch, uncertainty, or dependency for the human. Do not
expand scope, access another repository, deploy, or weaken these rails to make it
fit.
