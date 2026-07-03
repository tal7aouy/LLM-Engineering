# Notes MCP Server

A minimal, runnable [Model Context Protocol](https://modelcontextprotocol.io)
server that exposes a notes notebook as **tools** and **resources**.

Connect it to Claude Desktop, Cursor, Windsurf, or any MCP-compatible host.

## Setup

```bash
cd mcp-servers/notes-server
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python server.py
```

## Connect from Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS):

```json
{
  "mcpServers": {
    "notes": {
      "command": "python",
      "args": ["/absolute/path/to/mcp-servers/notes-server/server.py"]
    }
  }
}
```

Restart Claude Desktop → you'll see the `notes` server with `add_note` tool
and `notes://latest` resource.

## Tools exposed

| Tool        | Args        | Returns            |
| ----------- | ----------- | ------------------ |
| `add_note`  | `text: str` | Confirmation       |
| `list_notes`| —           | All notes          |
| `search_notes` | `query: str` | Matching notes  |

## Resources exposed

| URI               | Returns              |
| ----------------- | -------------------- |
| `notes://latest`  | Most recent note     |
| `notes://count`   | Number of notes      |

## Debug

```bash
# Inspect the server without a host
npx @modelcontextprotocol/inspector python server.py
```
