# Short Video Operations

This repository contains reusable short-video production skills and project data.

- Always require a `client_id` and `project_id` before producing client-facing content.
- Load the matching client profile before writing scripts or selecting assets.
- Keep client assets and outputs isolated under their own directories.
- Never invent product facts, prices, addresses, credentials, repair results, or customer claims.
- Prefer real footage for products, repairs, before/after evidence, and other factual demonstrations.
- Do not call paid generation APIs, publish content, or send external messages without explicit authorization for that action.
- Require human approval before publication.
- Store secrets only in environment variables or an approved secret manager; never commit them.
- Write machine-readable artifacts as UTF-8 JSON. Write human review artifacts as Markdown.

