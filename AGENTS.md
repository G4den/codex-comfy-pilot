# Comfy Pilot Guidelines

## Working With ComfyUI Workflows

When creating or modifying ComfyUI workflows, follow these practices:

### Node titles

Always assign descriptive custom titles to nodes when creating them. Prefer labels like:

- `CLIPTextEncode` -> `Positive Prompt`
- `KSampler` -> `Initial Generation`
- `LoadImage` -> `Reference Photo`
- `VAEDecode` -> `Final Decode`
- `ImageScale` -> `Upscale 2x`

### Node layout

Position nodes left-to-right following data flow:

- Loaders on the left (`x` around `100-300`)
- Processing in the middle (`x` around `400-700`)
- Output and preview nodes on the right (`x` around `800+`)
- Keep related nodes vertically aligned
- Leave at least `20px` of padding between nodes

When placing a node directly below another node, match the width of the node above it where practical.

Load 3D and animation nodes expand after creation. Leave at least `200px` of extra vertical spacing below them.

### Place new node groups in view

When creating nodes that are not connected to the existing workflow, use `place_in_view: true` so the user sees them immediately.

Use it for:

- New workflows
- Separate branches
- Standalone utility node groups

Do not use it for:

- Nodes that attach to an existing chain
- Moving existing nodes

### Batch graph changes

Use `edit_graph` for graph modifications so related operations stay together in one tool call.

Typical operations:

- `create`
- `set`
- `connect`
- `move`
- `resize`
- `delete`

Use `ref` values when creating multiple nodes in a batch so later operations can reference newly-created nodes.

### Running workflows

- Use `run(action="queue")` to execute.
- Use `run(action="interrupt")` to stop.
- Use `get_status(include=["queue", "system", "history"])` for queue and execution state.

### Searching for nodes

Search minimally first. Do not request `inputs` and `outputs` on broad searches.

Recommended pattern:

1. Search by keyword with default fields.
2. Pick likely matches from name and category.
3. Request detailed fields only for the small set of nodes you actually plan to use.

### Connections

- Use `get_node_info` when slot layout is unclear.
- Slot indices are zero-based.
- Match data types carefully when wiring nodes together.

### Previewing results

When the user wants to inspect output, add preview nodes where appropriate:

- Image outputs -> Preview Image
- Text or debug outputs -> available text preview node
- 3D outputs -> Preview 3D if available

If the workflow change is lightweight, run it automatically after wiring the preview.

Usually safe to auto-run:

- Debug and text preview nodes
- Metadata extraction
- Math and utility nodes
- Camera or layout calculations

Ask first before auto-running:

- KSampler or other generation-heavy paths
- Model-loading work
- GPU-intensive operations

### Finding preview nodes

Preview nodes vary by installation. Search first instead of assuming a node exists.

Common examples include:

- `PreviewAny`
- `ShowText|pysssss`

### Package management

Prefer `uv` for Python package and environment management when it is available.

Check first:

```bash
which uv
```

If `uv` exists, prefer:

- `uv pip install <package>`
- `uv venv`
- `uv sync`

If `uv` is not available, ask before installing it or falling back to another package manager.
