"""Tests for Codex route selection and legacy fallback in mcp_server."""

import importlib.util
import os
import sys
from unittest.mock import patch


_spec = importlib.util.spec_from_file_location(
    "mcp_server_routes",
    os.path.join(os.path.dirname(__file__), "..", "mcp_server.py"),
)
mcp_server = importlib.util.module_from_spec(_spec)
sys.modules["mcp_server_routes"] = mcp_server
_spec.loader.exec_module(mcp_server)


def test_make_plugin_request_uses_codex_route_first():
    with patch.object(mcp_server, "make_request", return_value={"ok": True}) as mock_request:
        result = mcp_server.make_plugin_request("/workflow")

    assert result == {"ok": True}
    mock_request.assert_called_once_with("/codex/workflow", method="GET", data=None, timeout=None)


def test_make_plugin_request_falls_back_to_legacy_route():
    with patch.object(
        mcp_server,
        "make_request",
        side_effect=[{"error": "missing"}, {"ok": True}],
    ) as mock_request:
        result = mcp_server.make_plugin_request("/graph-command", method="POST", data={"x": 1})

    assert result == {"ok": True}
    assert mock_request.call_count == 2
    assert mock_request.call_args_list[0].args == ("/codex/graph-command",)
    assert mock_request.call_args_list[0].kwargs == {"method": "POST", "data": {"x": 1}, "timeout": None}
    assert mock_request.call_args_list[1].args == ("/claude-code/graph-command",)
    assert mock_request.call_args_list[1].kwargs == {"method": "POST", "data": {"x": 1}, "timeout": None}
