---
name: client-brand-context
description: Load and validate one short-video client's brand, audience, offers, language, restrictions, and asset requirements. Use before creating or reviewing client-facing content in a multi-client workspace.
---

# Client brand context

Require `client_id` and `project_id`. Read only the matching files under `clients/<client_id>/` and `projects/<project_id>/`.

Validate that the project belongs to the client. Stop on a mismatch or missing profile rather than borrowing another client's data.

Return a compact context containing:

- verified brand and offer facts;
- target audience and platform;
- language, tone, pronunciation, and calls to action;
- prohibited claims and required disclaimers;
- real footage that must be supplied;
- unresolved questions that affect accuracy.

Never fill missing prices, addresses, credentials, repair outcomes, or product claims from general knowledge. Mark them as missing.

Use `scripts/validate_workspace.py` when changing client or project JSON.

