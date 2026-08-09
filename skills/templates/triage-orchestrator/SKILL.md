---
name: triage-orchestrator
description: >
  The pipeline driver for personal software projects. It processes manual V1
  intake tasks, scores, researches, routes, proposes, and starts approved work.
metadata:
  hermes:
    tags: [triage, orchestrator, software-projects]
---

# Project orchestrator (thin driver)

> **Design contract:** fat engine, thin skill. Use `engine/` for deterministic
> deduplication, score validation, task-chain construction, workspace selection,
> and routing. Supply only judgment: rubric scoring, research interpretation,
> classification, architecture synthesis, and proposal prose.

V1 uses a manually created `intake` Kanban task whose body is the path to a
report formatted by `skills/templates/project-intake/SKILL.md`. Do not create
scouts, cron jobs, profiles, messaging integrations, GitHub automation,
deployments, or production integrations as part of this workflow.

All commands run from the repository root with `triage.yaml` present.

## Procedure

### 1. Parse and persist intake

Read the report and parse it with `engine.intake_parser.parse_intake_report()`.
For each new candidate, create a vault item with its engine-required fields and
generic metadata:

```python
item = engine.vault.create_item(
    slug=<slug>,
    title=candidate.title,
    sources=candidate.sources,
    body=<intake summary>,
    attributes=candidate.attributes,
)
```

`Attributes:` metadata is generic and persisted in item frontmatter. The
`project_type_hint` is only the submitter's expectation; do not route from it.

### 2. Deduplicate and score

Use `TriageEngine.dedup()` for every candidate. For new items, use
`TriageEngine.rubric_prompt()` and score the configured dimensions honestly.
Pass the breakdown to `TriageEngine.score()` and save the result on the item.

- Below threshold: shelve without a proposal.
- At or above threshold: continue to research.

### 3. Research fan-out and authoritative classification

Create the triage root task and use `TriageEngine.research_specs()` to build the
parallel research lanes. The `project_classification` lane must emit exactly one
configured value at `project_classification.project_type`:

- `website`, `web_app`, `mobile_app`, or `automation` → `software_project`
- `research_only` → `research_only`
- `shelve` → `shelve`

Use `TriageEngine.route()` to resolve the emitted classification. Never route
from `project_type_hint` alone.

### 4. Pre-gate synthesis, architecture, and proposal

Use `TriageEngine.prep_specs()` for the selected path. The software-project
chain is `requirements_synthesis` then `solution_architecture`; the built-in
`propose` step is the implementation proposal and must not be duplicated as a
prep stage.

Draft the selected proposal template after prep completes. Record:

- complexity: low / medium / high
- implementation effort: small / medium / large
- expected external costs: none / low / medium / high
- confidence: low / medium / high
- major uncertainties

Do not present precise LLM-generated time estimates. Set item status to
`awaiting_approval` and present the proposal through the manually handled V1
gate. Never auto-approve.

### 5. Approval and fulfillment

When the human provides an approval, modification, or shelving instruction, use
the existing `proposal_actions.py` handler. On approval it creates the shared,
persistent post-gate chain. Do not change that workspace to scratch.

For `software_project`, the fulfillment stages are:

```
development → testing → review → documentation_delivery
```

For `research_only`, they are:

```
research → review → documentation_delivery
```

Workers must obey the inlined scope rails and deliverable specifications. The
final delivery stage produces the required record in the persistent workspace;
it does not deploy, publish, push, or configure external delivery systems.

## Rules

- Only the orchestrator writes vault item files and creates child tasks.
- Do not fabricate sources, test results, review outcomes, or external actions.
- Respect `paths/rails/*.md`, especially the Git, secret, repository, and Hermes
  configuration protections.
- If a task requires an unapproved external repository, deployment, credential,
  or broader scope, block it and explain why instead of guessing.