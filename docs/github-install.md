# Install from the private GitHub repository

Repository: `https://github.com/zhishenglian/short-video-ops.git`

## Windows

```powershell
git clone https://github.com/zhishenglian/short-video-ops.git 'D:\Agents\short-video-ops'
Set-Location 'D:\Agents\short-video-ops'
python scripts\validate_distribution.py .
```

Merge this into the active Hermes profile's `config.yaml` without creating a duplicate `skills` key:

```yaml
skills:
  external_dirs:
    - 'D:\Agents\short-video-ops\.agents\skills'
```

Start Hermes from `D:\Agents\short-video-ops`, run `/skills list`, and verify that `short-video-orchestrator` appears.

## macOS or Linux

```bash
git clone https://github.com/zhishenglian/short-video-ops.git "$HOME/agents/short-video-ops"
cd "$HOME/agents/short-video-ops"
python3 scripts/validate_distribution.py .
```

Add the following to the active Hermes profile's `config.yaml`:

```yaml
skills:
  external_dirs:
    - '${HOME}/agents/short-video-ops/.agents/skills'
```

Store API keys only in the active Hermes profile's `.env`. Run the documented dry-run before enabling paid providers or publishing.

