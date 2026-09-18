# Hermes adapter boundary

The core skills are platform-neutral Agent Skills. Do not create a Hermes-specific manifest until the exact Hermes distribution and loader contract are known.

A Hermes adapter must provide only these mappings:

1. Skill discovery path -> `.agents/skills/`
2. Shell/script execution -> repository `scripts/`
3. Environment secret lookup -> provider environment variables
4. Scheduled invocation -> `short-video-orchestrator`
5. Human approval callback -> approval record in the content version directory

The adapter must not duplicate business instructions from the skills. If Hermes cannot read Agent Skills directly, translate its invocation into the same input and output contracts rather than maintaining a second workflow.

