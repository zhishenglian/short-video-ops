---
name: video-assembly
description: Build a deterministic edit manifest and render short-video assets into review files with narration, matched visuals, subtitles, branding, and audio. Use after required media assets exist; not for creative approval or publishing.
---

# Video assembly

Create `edit-manifest.json` before rendering. It must identify the approved script version and every input asset by path or immutable URL.

The timeline must specify:

- shot in/out times;
- crop and target aspect ratio;
- narration and background audio levels;
- subtitle text and timing;
- brand overlays, contact details, and safe margins;
- transitions only where they improve comprehension.

Match visuals to the spoken sentence. Do not cover a factual claim with an unrelated generic shot.

Render review copies separately from final exports. Never overwrite an approved artifact; increment the version. Record tool versions and render settings so the output can be reproduced.

