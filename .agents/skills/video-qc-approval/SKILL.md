---
name: video-qc-approval
description: Review a short-video version for client accuracy, audiovisual quality, platform fit, consent, and publication readiness, then prepare a human approval package. Use before delivery or publication.
---

# Video quality control and approval

Run two review layers.

## Automated checks

- expected duration, resolution, aspect ratio, frame rate, and playable audio;
- subtitle coverage, spelling, contact details, and safe margins;
- missing, duplicated, frozen, silent, or corrupt segments;
- artifact identity matches `client_id`, `project_id`, and version.

## Editorial checks

- spoken claims match verified client facts;
- visuals match the narration and AI illustrations are not presented as evidence;
- language and pronunciation are natural for the target audience;
- logos, music, people, voices, and footage have appropriate permission;
- call to action is accurate and not misleading.

Return pass, pass-with-notes, or fail with time-coded findings. Only a human approval record may move a video to `approved`. Approval of one version never applies to a later render.

