# Data contracts

## Client profile

Required fields:

- `client_id`, `brand_name`, `industry`, `default_language`
- `target_audiences`, `content_pillars`, `calls_to_action`
- `required_real_footage`, `prohibited_claims`

Optional fields include platform targets, tone, pronunciation notes, contact details, legal disclaimers, and visual rules.

## Project

Required fields:

- `project_id`, `client_id`, `name`, `objective`, `platforms`
- `status`, `created_at`, `content_ids`

## Content item

Required fields:

- `content_id`, `client_id`, `project_id`, `status`, `version`
- `topic`, `target_duration_seconds`, `language`, `platforms`

Generated artifacts should be stored under:

`projects/<project_id>/content/<content_id>/v<version>/`

Recommended files:

- `brief.json`
- `script.md`
- `storyboard.json`
- `asset-plan.json`
- `edit-manifest.json`
- `qc-report.json`
- `approval.json`

## Provider adapter result

Every provider adapter returns JSON with:

- `provider`, `operation`, `status`
- `request_id`
- `billable_units` and `estimated_cost` when available
- `artifacts`
- `error` when unsuccessful

Valid statuses are `queued`, `running`, `succeeded`, `failed`, and `canceled`.

