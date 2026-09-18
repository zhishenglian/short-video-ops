---
name: short-video-orchestrator
description: Coordinate an identified client's short-video job across context loading, topic planning, script approval, media production, editing, and final review. Use for end-to-end production status or execution; publishing and paid calls still require separate authorization.
---

# Short-video orchestrator

Require `client_id`, `project_id`, and either `content_id` or an explicit request to create one.

Read `specs/workflow.md` and follow the state contract. Invoke only the skill needed for the current state:

- context: `client-brand-context`
- planning: `topic-content-planner`
- script and shots: `script-storyboard`
- media requests: `media-production`
- edit: `video-assembly`
- review: `video-qc-approval`

At each transition, write the next artifact, report what changed, and stop at an approval gate. Do not assume approval from silence or from approval of another version.

Default to dry-run provider configuration. Never expose secret values in logs or artifacts. Paid API calls, external messages, and publication require authorization for that action.

When a step fails, preserve completed artifacts, record a concise failure reason, and identify the minimal action required to continue. Do not restart the whole job unnecessarily.

