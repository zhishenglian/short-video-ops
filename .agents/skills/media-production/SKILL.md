---
name: media-production
description: Convert an approved storyboard into a provider-neutral media production plan and, when explicitly authorized, call configured avatar, voice, image, or video adapters. Use after script approval; do not publish content.
---

# Media production

Confirm the exact approved script version and provider configuration before creating media.

For every shot:

- prefer supplied real footage when factual accuracy matters;
- select an enabled provider compatible with the requested asset type;
- record prompt, input references, consent status, duration, aspect ratio, and expected cost;
- require explicit authorization before calling a paid provider;
- preserve provider request IDs and returned metadata.

Use dry-run mode by default. In dry-run mode, create the request manifests but make no external calls.

Real-person avatars and cloned voices require recorded consent. Do not attempt to bypass provider identity or likeness safeguards.

Retry transient failures at most twice. Do not automatically regenerate solely to chase subjective quality when that incurs cost; return candidates for review.

