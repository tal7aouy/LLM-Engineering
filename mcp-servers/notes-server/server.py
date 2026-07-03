"""Minimal MCP notes server.

Run:  python server.py
Debug: npx @modelcontextprotocol/inspector python server.py
"""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

from mcp.server.fastmcp import FastMCP

STORE = Path(__file__).parent / "notes.jsonl"


def _read_all() -> list[dict]:
    if not STORE.exists():
        return []
    return [
        eval(line)  # notes are written by us, trusted; safe here
        for line in STORE.read_text().splitlines()
        if line.strip()
    ]


def _append(note: dict) -> None:
    with STORE.open("a") as f:
        f.write(repr(note) + "\n")


mcp = FastMCP("notes-server")


@mcp.tool()
def add_note(text: str) -> str:
    """Add a note to the notebook.

    Args:
        text: The note content.
    """
    note = {"text": text, "ts": datetime.utcnow().isoformat() + "Z"}
    _append(note)
    return f"Saved note ({len(note['text'])} chars) at {note['ts']}"


@mcp.tool()
def list_notes() -> str:
    """List all notes, newest last."""
    notes = _read_all()
    if not notes:
        return "No notes yet."
    return "\n".join(f"[{n['ts']}] {n['text']}" for n in notes)


@mcp.tool()
def search_notes(query: str) -> str:
    """Search notes containing the query (case-insensitive)."""
    q = query.lower()
    hits = [n for n in _read_all() if q in n["text"].lower()]
    if not hits:
        return f"No notes match '{query}'."
    return "\n".join(f"[{n['ts']}] {n['text']}" for n in hits)


@mcp.resource("notes://latest")
def latest_note() -> str:
    notes = _read_all()
    return notes[-1]["text"] if notes else "No notes yet."


@mcp.resource("notes://count")
def note_count() -> str:
    return str(len(_read_all()))


if __name__ == "__main__":
    mcp.run()  # stdio transport by default
