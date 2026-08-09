---
name: project-intake
description: >
  Manual V1 intake template for the personal software-project workflow. Records a
  project request as a report and a manually created Kanban intake task.
metadata:
  hermes:
    tags: [triage, intake, manual]
---

# Project intake (manual V1)

> This is a temporary manual intake mechanism. It deliberately does not create
> Hermes profiles, cron jobs, scouts, messaging, GitHub automation, deployments,
> or production integrations. Future intake may come directly from Hermes,
> Obsidian, or a CLI/helper without manually constructing Kanban tasks.

## Create an intake report

Save one Markdown report at:

```
work/vault/intake/<UTC-timestamp>-manual.md
```

Use this exact structure:

```
source: manual
captured_at: <UTC timestamp>

## Candidate: <project title>
Claim: <one-line project request>
Sources:
  - url: <reference URL, repository URL, or manual intake>
    quote: "<optional supporting context>"
Why it may matter: <one line>
Attributes:
  objective: <desired outcome>
  target_users: <who benefits>
  constraints: <budget, time, technology, or safety constraints>
  existing_repository: <none or reference only; V1 does not operate in it automatically>
  project_type_hint: <website|web_app|mobile_app|automation|research_only|shelve>
```

`project_type_hint` records the submitter's expectation only. The
`project_classification` research lane is authoritative for routing.

## Create the intake task

Manually create one Kanban task on the `personal-projects` board:

- title: `intake: manual <UTC-date>`
- assignee: `project-orchestrator`
- body: the path to the report created above
- parents: none, so the task begins ready

The orchestrator parses the report, persists generic `Attributes:` metadata,
deduplicates, scores, researches, classifies, and creates an approval proposal.

## Do not

- Do not treat a project type hint as an authoritative route decision.
- Do not add fake `sources:` entries, scout schedules, or cron jobs for V1.
- Do not include credentials, secrets, private tokens, or unapproved production
  details in the report.
