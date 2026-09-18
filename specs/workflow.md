# Workflow contract

## States

`brief` -> `script_review` -> `asset_planning` -> `asset_generation` -> `editing` -> `final_review` -> `approved` -> `scheduled` -> `published` -> `analyzed`

`blocked` may be entered from any state. A blocked job must record a reason and the action needed to continue.

## Approval gates

- Moving from `script_review` to `asset_planning` requires script approval.
- Moving from `final_review` to `approved` requires final-video approval.
- Moving from `approved` to `scheduled` or `published` requires explicit publication authorization.
- An approval records approver, timestamp, artifact version, and optional notes.

## Job identity

Every artifact must include:

- `client_id`
- `project_id`
- `content_id`
- `version`

Never infer one client's identity from another project's files.

## Failure behavior

- Paid generation: retry at most twice for transient provider failures, then block the job.
- Validation or policy failure: do not retry automatically; return the exact failed checks.
- Missing factual footage: request the missing asset or mark the scene as illustrative.
- Publishing failure: never switch to browser automation automatically.

