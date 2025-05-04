# server.py
from mcp.server.fastmcp import FastMCP
import os
from datetime import datetime, timezone, timedelta

IST = timezone(timedelta(hours=5, minutes=30))  # Asia/Kolkata

# Create an MCP server
mcp = FastMCP("AI Sticky Notes")

NOTES_FILES = os.path.join(os.path.dirname(__file__),"notes.txt")

def ensure_notes_file_exists():
    """Ensure the notes file exists."""
    if not os.path.exists(NOTES_FILES):
        with open(NOTES_FILES, "w") as f:
            f.write("")


@mcp.tool()
def add_note(message: str) -> str:
    """
    Append a new note to the sticky notes file.
    Args:
        message (str): The note to be added.
    Returns:
        str: Confirmation message.
    """
    ensure_notes_file_exists()
    # Get the current time in IST
    local_now = datetime.now(IST)
    with open(NOTES_FILES, "a") as f:
        f.write(f"{local_now} - {message}\n")
    return "Note added!"


@mcp.tool()
def read_notes() -> str:
    """
    Read all notes from the sticky notes file.
    Returns:
        str: All notes.
    """
    ensure_notes_file_exists()
    with open(NOTES_FILES, "r") as f:
        notes = f.read().strip()
    return notes if notes else "No notes found."


@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Get the latest note from the sticky notes file.
    Returns:
        str: The latest nore, if not found, return a message.
    """
    ensure_notes_file_exists()
    with open(NOTES_FILES, "r") as f:
        notes = f.readlines()
    return notes[-1].strip() if notes else "No notes found."


@mcp.prompt()
def note_summary_prompt() -> str:
    """
    Generate a prompt asking the AI to summarize all current notes.

    Returns:
        str: A prompt string that includes all notes and asks for a summary.
             If no notes exist, a message will be shown indicating that.
    """
    ensure_notes_file_exists()
    with open(NOTES_FILES, "r") as f:
        notes = f.read().strip()
    return notes if notes else "No notes found."