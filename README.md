# AI Sticky Notes MCP Server

## Project Overview
This project is a basic implementation of an MCP (Model Context Protocol) server named "AI Sticky Notes." It allows users to manage sticky notes by adding, reading, and summarizing them. The server is built using the `FastMCP` from `MCP` framework.

## Features
- **Add Notes**: Append new notes to a file.
- **Read Notes**: Retrieve all stored notes.
- **Get Latest Note**: Fetch the most recent note.
- **Summarize Notes**: Generate a prompt summarizing all notes.

## Project Structure
- **main.py**: Contains the server logic and tools for managing notes.
- **notes.txt**: Stores all the sticky notes.
- **pyproject.toml**: Configuration file for managing dependencies and project metadata.

## Prerequisites
- Python 3.11 or higher
- Virtual environment setup

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-URL>
   cd AI-Sticky-Notes-MCP-Server
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

3. Install dependencies using `uv`:
   ```bash
   uv sync
   ```

## Running the Server
To start the MCP server using `uv`, run the following command:
```bash
uv run mcp install main.py
```
