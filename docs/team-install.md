# Install for Hermes Agent

## Requirements

- Hermes Agent with external skill directory support
- Git
- Python 3.10 or later

## Clone

Choose a stable local directory. Do not clone inside a temporary or downloads folder.

Windows PowerShell:

```powershell
git clone <PRIVATE_REPOSITORY_URL> 'D:\Agents\short-video-ops'
Set-Location 'D:\Agents\short-video-ops'
python scripts\validate_workspace.py .
```

macOS or Linux:

```bash
git clone <PRIVATE_REPOSITORY_URL> "$HOME/agents/short-video-ops"
cd "$HOME/agents/short-video-ops"
python3 scripts/validate_workspace.py .
```

## Connect Hermes

Resolve the active Hermes home from `HERMES_HOME`; if unset, consult the local Hermes installation. Edit that profile's `config.yaml` and merge this entry into the existing `skills` section.

Windows example:

```yaml
skills:
  external_dirs:
    - 'D:\Agents\short-video-ops\.agents\skills'
```

macOS or Linux example:

```yaml
skills:
  external_dirs:
    - '${HOME}/agents/short-video-ops/.agents/skills'
```

Do not create a second `skills:` key. Preserve all existing values under that section.

Start Hermes from the repository root so repository-relative scripts and project data resolve correctly. In Hermes, run `/skills list` and verify that `short-video-orchestrator` is present.

## First dry-run

Use:

```text
/short-video-orchestrator

For client example-auto-repair and project example-campaign, prepare a 60-second
short-video job about tyre inspection. Dry-run only: do not call paid APIs, send
messages, or publish.
```

## Secrets

Copy only required variable names from `.env.example` into the active Hermes profile's `.env`. Never copy another operator's secrets and never commit `.env`.

## Update

```powershell
git -C 'D:\Agents\short-video-ops' pull --ff-only
python 'D:\Agents\short-video-ops\scripts\validate_workspace.py' 'D:\Agents\short-video-ops'
```

Use tagged releases for production. If an update fails validation, remain on the previous tag and notify the maintainer.

## Editing policy

Treat the shared checkout as read-only for ordinary operators. Propose Skill changes through a reviewed branch or pull request. Client-private data should live outside the shared repository or only in an access-controlled client repository.

