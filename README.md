<div align="center">

# 🤖 Model Context Protocol Server

**A production-ready MCP server built with the official Python SDK**  
**exposing 17 tools, 3 resources, and 2 AI prompts to any LLM application.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![MCP](https://img.shields.io/badge/MCP-Python%20SDK-8B5CF6)](https://modelcontextprotocol.io)
[![License](https://img.shields.io/badge/License-MIT-22C55E)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-22C55E)](myserver.py)

</div>

---

## 📌 What Is This?

This project is a **fully-featured MCP (Model Context Protocol) server** built with the official [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk).

**MCP** is an open standard by Anthropic that lets you expose tools, data, and prompts to any LLM application — Claude, ChatGPT, or your own AI agent. Think of it as a **REST API designed specifically for AI**.

| Concept | What it does |
|---|---|
| **Tools** | Functions the LLM can call (math, text, notes, users, utilities) |
| **Resources** | Data the LLM can read via URI templates (like REST GET endpoints) |
| **Prompts** | Reusable AI prompt templates with dynamic inputs |

---

## ✨ What's Inside

```
ProfessionalServer
├── 🔢 Math Tools      →  add · subtract · multiply · divide · power
├── 📝 Text Tools      →  greet · reverse_text · word_count · to_uppercase · to_lowercase
├── 🗒️  Note Manager   →  create_note · get_note · list_notes · delete_note
├── 👤 User Manager    →  create_user · get_user · list_users
├── 🛠️  Utilities      →  current_datetime · calculate_bmi · convert_temperature
├── 📦 Resources       →  note://{title} · user://{username} · server://info
└── 💬 Prompts         →  summarize_note · introduce_user
```

---

## 🚀 Quick Start

### 1 — Prerequisites

- Python **3.10+** → [download](https://www.python.org/downloads/)
- Verify: `python --version`

### 2 — Install the MCP CLI

```bash
pip install "mcp[cli]"
```

> Prefer `uv` (faster)?
> ```bash
> pip install uv
> uv add "mcp[cli]"
> ```

### 3 — Clone this repo

```bash
git clone https://github.com/yasar2005/model-context-protocol-server.git
cd model-context-protocol-server
```

### 4 — Run the server

```bash
mcp dev myserver.py
```

This starts the server **and** opens the MCP Inspector UI automatically.

### 5 — Open the Inspector

Go to **`http://localhost:6274`** in your browser — a full interactive dashboard to test every tool, resource, and prompt.

---

## 🖥️ Using the MCP Inspector

### ▶ Run a Tool
1. Click **Tools** tab → **List Tools**
2. Click any tool to expand it
3. Fill in the inputs → click **Run Tool**
4. See the result in the **Response** panel

### 📦 Read a Resource
1. Click **Resources** tab → **List Templates**
2. Select a template (e.g. `note://{title}`)
3. Enter the variable (e.g. `shopping-list`) → **Read Resource**

### 💬 Use a Prompt
1. Click **Prompts** tab → **List Prompts**
2. Select a prompt → fill in the argument → **Get Prompt**
3. Copy the output into any AI chat

---

## 🛠️ Tools Reference

### 🔢 Math Tools

| Tool | Inputs | Example |
|---|---|---|
| `add` | `a`, `b` | `add(10, 5)` → `15.0` |
| `subtract` | `a`, `b` | `subtract(10, 3)` → `7.0` |
| `multiply` | `a`, `b` | `multiply(4, 5)` → `20.0` |
| `divide` | `a`, `b` | `divide(20, 4)` → `5.0` |
| `power` | `base`, `exponent` | `power(2, 10)` → `1024.0` |

### 📝 Text Tools

| Tool | Inputs | Example |
|---|---|---|
| `greet` | `name`, `language` | `greet("Alice", "spanish")` → `¡Hola, Alice!` |
| `reverse_text` | `text` | `"hello"` → `"olleh"` |
| `word_count` | `text` | Returns `{words, characters, lines}` |
| `to_uppercase` | `text` | `"hello"` → `"HELLO"` |
| `to_lowercase` | `text` | `"HELLO"` → `"hello"` |

Supported languages for `greet`: `english` · `spanish` · `french` · `german` · `japanese`

### 🗒️ Note Manager

| Tool | Inputs | What it does |
|---|---|---|
| `create_note` | `title`, `content` | Saves a note to memory |
| `get_note` | `title` | Retrieves note content |
| `list_notes` | _(none)_ | Lists all note titles |
| `delete_note` | `title` | Permanently removes a note |

### 👤 User Manager

| Tool | Inputs | What it does |
|---|---|---|
| `create_user` | `username`, `email`, `role` | Registers a new user |
| `get_user` | `username` | Returns full profile |
| `list_users` | _(none)_ | Lists all usernames |

Supported roles: `user` · `admin` · `editor`

### 🛠️ Utility Tools

| Tool | Inputs | Example Output |
|---|---|---|
| `current_datetime` | _(none)_ | `"2024-01-15 14:30:45"` |
| `calculate_bmi` | `weight_kg`, `height_m` | `{bmi: 22.86, category: "Normal weight ✅"}` |
| `convert_temperature` | `value`, `from_unit` | `{celsius: 100, fahrenheit: 212.0, kelvin: 373.15}` |

BMI categories: `Underweight 🔵` · `Normal weight ✅` · `Overweight 🟡` · `Obese 🔴`  
Temperature units: `celsius` · `fahrenheit` · `kelvin`

---

## 📦 Resources

| URI Template | Input | Returns |
|---|---|---|
| `note://{title}` | Note title | Full note content |
| `user://{username}` | Username | Full user profile |
| `server://info` | _(none)_ | Live server stats & status |

---

## 💬 Prompts

| Prompt | Input | Output |
|---|---|---|
| `summarize_note` | `title` | AI-ready prompt to summarize a saved note |
| `introduce_user` | `username` | AI-ready prompt to write a professional user intro |

---

## 🏗️ Project Structure

```
model-context-protocol-server/
├── myserver.py          ← Main MCP server (all tools, resources, prompts)
├── pyproject.toml       ← Project config & dependencies
├── src/mcp/             ← MCP Python SDK source
├── examples/            ← Example servers and clients
├── docs/                ← Full SDK documentation
└── tests/               ← Test suite
```

> **Data storage:** In-memory Python dicts. Data persists while the server is running — restart clears it.  
> **Transport:** `stdio` (default via `mcp dev`) — compatible with Claude Desktop and any MCP host.

---

## 🔌 Connect to Claude Desktop

Add this to your Claude Desktop config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "professional-server": {
      "command": "python",
      "args": ["path/to/myserver.py"]
    }
  }
}
```

Claude will then have access to all 17 tools directly in chat.

---

## 📋 Requirements

- Python **3.10+**
- `mcp[cli]` package

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

Built with the [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) &nbsp;·&nbsp; [Model Context Protocol](https://modelcontextprotocol.io) &nbsp;·&nbsp; [MCP Inspector](https://github.com/modelcontextprotocol/inspector)

</div>
