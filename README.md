# Comfy Pilot

[![Stars](https://img.shields.io/github/stars/ConstantineB6/Comfy-Pilot)](https://github.com/ConstantineB6/Comfy-Pilot/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ComfyUI Registry](https://img.shields.io/badge/ComfyUI-Registry-blue)](https://registry.comfy.org/publishers/constantine/nodes/comfy-pilot)

Talk to your ComfyUI workflows. Comfy Pilot gives Codex CLI direct access to see, edit, and run your workflows, with an embedded terminal right inside ComfyUI on Unix-like systems.

![Comfy Pilot](thumbnail.jpg)

## Why?

Building ComfyUI workflows usually means searching for nodes, wiring them manually, and tweaking values one at a time. With Comfy Pilot, you can describe the workflow you want instead:

- "Build me an SDXL workflow with ControlNet"
- "Look at the output and increase the detail"
- "Download the FLUX schnell model and wire up a starter workflow"

Comfy Pilot syncs the live graph from the browser to an MCP server so Codex can inspect it, edit it, and run it.

## Installation

### CLI (Recommended)

```bash
comfy node install comfy-pilot
```

### ComfyUI Manager

1. Open ComfyUI.
2. Click **Manager** -> **Install Custom Nodes**.
3. Search for `Comfy Pilot`.
4. Click **Install**.
5. Restart ComfyUI.

### Git Clone

```bash
cd ~/Documents/ComfyUI/custom_nodes
git clone https://github.com/ConstantineB6/comfy-pilot.git
```

## Requirements

- ComfyUI
- Python 3.8+
- Codex CLI

If `codex` is missing and `npm` is available, the plugin will try to install Codex automatically with:

```bash
npm install -g @openai/codex
```

You still need to authenticate Codex separately:

```bash
codex login
```

## Features

- **MCP Server**: Gives Codex CLI direct access to view, edit, and run your ComfyUI workflows.
- **Embedded Terminal**: Runs Codex CLI inside ComfyUI on macOS and Linux.
- **Workflow Sync**: Keeps the live browser graph available to the MCP server.
- **Image Viewing**: Lets Codex inspect images from Preview Image and Save Image nodes.
- **Graph Editing**: Create, delete, move, resize, connect, and configure nodes programmatically.

## Usage

1. Restart ComfyUI after installation.
2. Open the floating `Codex CLI` window from the top-right corner or canvas context menu.
3. Comfy Pilot registers its MCP server with Codex automatically when the `codex` CLI is available.
4. Ask Codex to help with your workflow:
   - `What nodes are in my current workflow?`
   - `Add a KSampler node connected to my checkpoint loader.`
   - `Look at the preview image and tell me what you see.`
   - `Run the workflow up to node 5.`

### Windows note

The embedded terminal is still disabled on Windows in this plugin build. The MCP bridge still works, so you can run `codex` in a separate terminal after Comfy Pilot configures the MCP server.

## MCP Tools

The MCP server provides these tools to Codex:

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
| `search_custom_nodes` | Search ComfyUI Manager registry for custom nodes |
| `install_custom_node` | Install a custom node from the registry |
| `uninstall_custom_node` | Uninstall a custom node |
| `update_custom_node` | Update a custom node to the latest version |
| `download_model` | Download models from Hugging Face, CivitAI, or direct URLs |

## Architecture

- Browser frontend: `js/codex-cli.js`
- Backend plugin: `__init__.py`
- MCP server: `mcp_server.py`
- Codex instructions: `AGENTS.md`

The active browser bridge uses:

- WebSocket: `/ws/codex-terminal`
- HTTP API: `/codex/*`

Legacy `/ws/claude-terminal` and `/claude-code/*` routes are still registered as compatibility aliases.

## Troubleshooting

### `codex` not found

Install Codex CLI:

```bash
npm install -g @openai/codex
codex login
```

If `npm` is not installed, install Node.js first.

### MCP server not connecting

The plugin auto-configures MCP on startup with `codex mcp add`. If that fails, add this to `~/.codex/config.toml`:

```toml
[mcp_servers.comfyui]
command = "python"
args = ["/path/to/comfy-pilot/mcp_server.py"]
```

Then restart Codex.

### Terminal disconnected

Click the reload button in the floating terminal, or check the ComfyUI console for plugin startup errors.

## License

MIT
