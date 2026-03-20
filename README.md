# Comfy Pilot

[![Stars](https://img.shields.io/github/stars/ConstantineB6/Comfy-Pilot)](https://github.com/ConstantineB6/Comfy-Pilot/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Comfy Pilot connects ComfyUI to Codex CLI. It syncs your live workflow from the browser to an MCP server so Codex can inspect it, edit it, run it, and look at generated images.

This repo is intended to be used locally as a custom node. It is not documented here as a registry or store install.

![Comfy Pilot](thumbnail.jpg)

## What it does

- Exposes your current ComfyUI workflow to Codex through MCP.
- Lets Codex create, move, connect, configure, and delete nodes.
- Lets Codex inspect images from Preview Image and Save Image nodes.
- Provides an embedded Codex terminal on macOS and Linux.
- Keeps working on Windows through the MCP bridge, but without the embedded terminal.

## Local install

Clone this repo into your ComfyUI `custom_nodes` folder.

### Windows

```powershell
cd C:\Users\gade1\Documents\ComfyUI\custom_nodes
git clone C:\Users\gade1\Documents\GitHub\codex-comfy-pilot
```

If you prefer a symlink so edits in this repo are reflected immediately:

```powershell
New-Item -ItemType SymbolicLink `
  -Path "C:\Users\gade1\Documents\ComfyUI\custom_nodes\codex-comfy-pilot" `
  -Target "C:\Users\gade1\Documents\GitHub\codex-comfy-pilot"
```

### macOS / Linux

```bash
cd ~/ComfyUI/custom_nodes
git clone /path/to/codex-comfy-pilot
```

After that:

1. Restart ComfyUI.
2. Make sure Codex CLI is installed.
3. Make sure Codex is logged in.

## Requirements

- ComfyUI
- Python 3.8+
- Codex CLI
- `git` for local clone-based install

Install Codex CLI if needed:

```bash
npm install -g @openai/codex
codex login
```

If `codex` is missing and `npm` is available, the plugin will also try to install Codex automatically on startup.

## How to use it

1. Start ComfyUI.
2. Open a workflow in the browser.
3. Let Comfy Pilot sync the workflow to its backend.
4. On macOS or Linux, use the embedded `Codex CLI` panel inside ComfyUI.
5. On Windows, open a separate terminal and run `codex` from there.

Example prompts:

- `What nodes are in my current workflow?`
- `Add a KSampler node connected to my checkpoint loader.`
- `Look at the preview image and tell me what you see.`
- `Run the workflow up to node 5.`

## Windows behavior

The embedded terminal is currently disabled on Windows in this build.

That means:

- The floating Codex panel may show `Terminal disconnected`.
- Clicking reload will not make the embedded terminal work on Windows.
- The MCP bridge can still work.
- You should run `codex` in a separate terminal window.

This is expected with the current implementation and is not, by itself, a sign that MCP failed.

## MCP setup

The plugin attempts to register its MCP server automatically with:

```bash
codex mcp add comfyui -- python /path/to/mcp_server.py
```

If automatic registration fails, add this manually to `~/.codex/config.toml`:

```toml
[mcp_servers.comfyui]
command = "python"
args = ["/path/to/comfy-pilot/mcp_server.py"]
```

Then restart Codex.

## Available tools

The MCP server exposes these tools to Codex:

| Tool | Description |
|------|-------------|
| `get_workflow` | Get the current workflow from the browser |
| `summarize_workflow` | Human-readable workflow summary |
| `get_node_types` | Search available node types with filtering |
| `get_node_info` | Get detailed info about a specific node type |
| `get_status` | Queue status, system stats, and execution history |
| `run` | Run workflow, optionally up to a specific node, or interrupt |
| `edit_graph` | Batch create, delete, move, connect, resize, and configure nodes |
| `view_image` | View images from Preview Image and Save Image nodes |
| `search_custom_nodes` | Search available custom nodes |
| `install_custom_node` | Install a custom node |
| `uninstall_custom_node` | Uninstall a custom node |
| `update_custom_node` | Update a custom node |
| `download_model` | Download models from Hugging Face, CivitAI, or direct URLs |

## Files

- `__init__.py`: ComfyUI plugin backend and routes
- `js/codex-cli.js`: browser frontend and embedded terminal UI
- `mcp_server.py`: MCP server exposed to Codex
- `AGENTS.md`: workflow guidance for Codex when operating on ComfyUI graphs

## Troubleshooting

### `codex` not found

Install Codex CLI and log in:

```bash
npm install -g @openai/codex
codex login
```

### `Terminal disconnected`

On Windows, this is expected because the embedded terminal is disabled.

On macOS or Linux, it usually means the WebSocket-backed terminal session failed to start. Check the ComfyUI console for plugin startup errors.

### MCP server not connecting

Check that:

- ComfyUI is running.
- This repo is installed inside `custom_nodes`.
- `codex` is installed and logged in.
- The MCP config exists in `~/.codex/config.toml` if auto-registration failed.

## License

MIT
