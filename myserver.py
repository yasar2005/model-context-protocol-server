"""
╔══════════════════════════════════════════════════════════════╗
║           🚀 PROFESSIONAL MCP SERVER                        ║
║           Built with Model Context Protocol SDK             ║
╠══════════════════════════════════════════════════════════════╣
║  CATEGORIES:                                                 ║
║  🔢 Math Tools       → add, subtract, multiply, divide       ║
║  📝 Text Tools       → greet, reverse, word_count, case      ║
║  🗒️  Note Manager    → create, read, list, delete notes      ║
║  👤 User Manager     → create, read, list users              ║
║  🛠️  Utilities       → datetime, BMI, temperature            ║
║  📦 Resources        → note://, user://, server://info       ║
║  💬 Prompts          → summarize_note, introduce_user        ║
╚══════════════════════════════════════════════════════════════╝

HOW TO USE IN MCP INSPECTOR:
  1. Click the "Tools" tab on the left
  2. Click "List Tools" to see all available tools
  3. Click any tool name to expand it
  4. Fill in the input fields shown
  5. Click "Run Tool" to execute
  6. See the result in the Response panel

HOW TO USE RESOURCES:
  1. Click the "Resources" tab
  2. Click "List Templates"
  3. Select a template (e.g. note://{title})
  4. Fill in the variable (e.g. title = "my-note")
  5. Click "Read Resource"

HOW TO USE PROMPTS:
  1. Click the "Prompts" tab
  2. Click "List Prompts"
  3. Select a prompt
  4. Fill in the arguments
  5. Click "Get Prompt" to generate the prompt text
"""

from datetime import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="ProfessionalServer")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 💾 IN-MEMORY DATA STORE
# (Data is stored while the server is running)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
notes: dict[str, str] = {}
users: dict[str, dict] = {}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔢 MATH TOOLS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@mcp.tool()
def add(a: float, b: float) -> float:
    """
    ➕ ADD TWO NUMBERS

    Adds two numbers and returns the result.

    INPUTS:
      a → First number  (e.g. 10)
      b → Second number (e.g. 5)

    EXAMPLE:
      a = 10, b = 5  →  Result: 15.0

    TRY IT: Enter any two numbers and click Run Tool.
    """
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """
    ➖ SUBTRACT TWO NUMBERS

    Subtracts b from a and returns the result.

    INPUTS:
      a → Number to subtract from (e.g. 10)
      b → Number to subtract      (e.g. 3)

    EXAMPLE:
      a = 10, b = 3  →  Result: 7.0

    TRY IT: Enter any two numbers and click Run Tool.
    """
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """
    ✖️ MULTIPLY TWO NUMBERS

    Multiplies two numbers together.

    INPUTS:
      a → First number  (e.g. 4)
      b → Second number (e.g. 5)

    EXAMPLE:
      a = 4, b = 5  →  Result: 20.0

    TRY IT: Enter any two numbers and click Run Tool.
    """
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float | str:
    """
    ➗ DIVIDE TWO NUMBERS

    Divides a by b. Returns an error if b is zero.

    INPUTS:
      a → Number to divide        (e.g. 20)
      b → Number to divide by     (e.g. 4)

    EXAMPLE:
      a = 20, b = 4  →  Result: 5.0
      a = 10, b = 0  →  Result: ❌ Error: Cannot divide by zero.

    TRY IT: Enter any two numbers and click Run Tool.
    """
    if b == 0:
        return "❌ Error: Cannot divide by zero."
    return a / b


@mcp.tool()
def power(base: float, exponent: float) -> float:
    """
    🔋 RAISE TO THE POWER

    Raises base to the power of exponent.

    INPUTS:
      base     → The base number     (e.g. 2)
      exponent → The power to raise  (e.g. 10)

    EXAMPLE:
      base = 2, exponent = 10  →  Result: 1024.0
      base = 3, exponent = 3   →  Result: 27.0

    TRY IT: Enter base and exponent, then click Run Tool.
    """
    return base ** exponent


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📝 TEXT TOOLS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@mcp.tool()
def greet(name: str, language: str = "english") -> str:
    """
    👋 GREET SOMEONE IN DIFFERENT LANGUAGES

    Generates a greeting message in the chosen language.

    INPUTS:
      name     → Person's name     (e.g. Alice)
      language → Language to use   (default: english)

    SUPPORTED LANGUAGES:
      english | spanish | french | german | japanese

    EXAMPLES:
      name = "Alice", language = "english"  →  Hello, Alice! Welcome!
      name = "Carlos", language = "spanish" →  ¡Hola, Carlos! ¡Bienvenido!
      name = "Yuki", language = "japanese"  →  こんにちは, Yuki! ようこそ!

    TRY IT: Type a name and pick a language, then click Run Tool.
    """
    greetings = {
        "english":  f"👋 Hello, {name}! Welcome!",
        "spanish":  f"👋 ¡Hola, {name}! ¡Bienvenido!",
        "french":   f"👋 Bonjour, {name}! Bienvenue!",
        "german":   f"👋 Hallo, {name}! Willkommen!",
        "japanese": f"👋 こんにちは, {name}! ようこそ!",
    }
    return greetings.get(language.lower(), f"👋 Hello, {name}!")


@mcp.tool()
def reverse_text(text: str) -> str:
    """
    🔄 REVERSE A TEXT STRING

    Reverses the characters in the given text.

    INPUTS:
      text → Any text string (e.g. "hello world")

    EXAMPLE:
      text = "hello"        →  Result: "olleh"
      text = "MCP Server"   →  Result: "revreS PCM"

    TRY IT: Type any text and click Run Tool.
    """
    return text[::-1]


@mcp.tool()
def word_count(text: str) -> dict:
    """
    🔢 COUNT WORDS, CHARACTERS & LINES

    Analyzes the given text and returns statistics.

    INPUTS:
      text → Any block of text (e.g. "Hello world. How are you?")

    RETURNS:
      words                → Total number of words
      characters           → Total characters (including spaces)
      characters_no_spaces → Characters without spaces
      lines                → Number of lines

    EXAMPLE:
      text = "Hello world"
      →  { words: 2, characters: 11, characters_no_spaces: 10, lines: 1 }

    TRY IT: Paste any text and click Run Tool.
    """
    return {
        "words": len(text.split()),
        "characters": len(text),
        "characters_no_spaces": len(text.replace(" ", "")),
        "lines": len(text.splitlines()) or 1,
    }


@mcp.tool()
def to_uppercase(text: str) -> str:
    """
    🔠 CONVERT TEXT TO UPPERCASE

    Converts all characters in the text to UPPERCASE.

    INPUTS:
      text → Any text (e.g. "hello world")

    EXAMPLE:
      text = "hello world"  →  Result: "HELLO WORLD"

    TRY IT: Type any text and click Run Tool.
    """
    return text.upper()


@mcp.tool()
def to_lowercase(text: str) -> str:
    """
    🔡 CONVERT TEXT TO LOWERCASE

    Converts all characters in the text to lowercase.

    INPUTS:
      text → Any text (e.g. "HELLO WORLD")

    EXAMPLE:
      text = "HELLO WORLD"  →  Result: "hello world"

    TRY IT: Type any text and click Run Tool.
    """
    return text.lower()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🗒️ NOTE MANAGER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@mcp.tool()
def create_note(title: str, content: str) -> str:
    """
    📝 CREATE A NEW NOTE

    Saves a note with a title and content to memory.

    INPUTS:
      title   → Unique name for the note  (e.g. "shopping-list")
      content → The body of the note      (e.g. "Milk, Eggs, Bread")

    EXAMPLE:
      title = "shopping-list", content = "Milk, Eggs, Bread"
      →  ✅ Note 'shopping-list' created successfully.

    NEXT STEPS:
      → Use get_note to read it back
      → Use list_notes to see all notes
      → Use note://{title} in Resources tab to view it

    TRY IT: Enter a title and content, then click Run Tool.
    """
    notes[title] = content
    return f"✅ Note '{title}' created successfully."


@mcp.tool()
def get_note(title: str) -> str:
    """
    📖 READ A NOTE

    Retrieves the content of a saved note by its title.

    INPUTS:
      title → The exact title of the note (e.g. "shopping-list")

    EXAMPLE:
      title = "shopping-list"  →  Result: "Milk, Eggs, Bread"
      title = "unknown"        →  Result: ❌ Note 'unknown' not found.

    PREREQUISITE:
      → First create a note using create_note tool

    TRY IT: Enter the note title and click Run Tool.
    """
    return notes.get(title, f"❌ Note '{title}' not found. Use create_note first.")


@mcp.tool()
def list_notes() -> list[str]:
    """
    📋 LIST ALL NOTES

    Returns a list of all saved note titles.

    INPUTS:
      (none required)

    EXAMPLE:
      →  ["shopping-list", "meeting-notes", "ideas"]
      →  ["📭 No notes yet. Use create_note to add one."]

    TRY IT: Just click Run Tool — no inputs needed.
    """
    return list(notes.keys()) if notes else ["📭 No notes yet. Use create_note to add one."]


@mcp.tool()
def delete_note(title: str) -> str:
    """
    🗑️ DELETE A NOTE

    Permanently removes a note from memory.

    INPUTS:
      title → The exact title of the note to delete (e.g. "shopping-list")

    EXAMPLE:
      title = "shopping-list"  →  ✅ Note 'shopping-list' deleted.
      title = "unknown"        →  ❌ Note 'unknown' not found.

    WARNING:
      This action cannot be undone while the server is running.

    TRY IT: Enter the note title and click Run Tool.
    """
    if title in notes:
        del notes[title]
        return f"✅ Note '{title}' deleted successfully."
    return f"❌ Note '{title}' not found. Use list_notes to see available notes."


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 👤 USER MANAGER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@mcp.tool()
def create_user(username: str, email: str, role: str = "user") -> str:
    """
    👤 CREATE A NEW USER

    Registers a new user with username, email, and role.

    INPUTS:
      username → Unique username   (e.g. "john_doe")
      email    → User's email      (e.g. "john@example.com")
      role     → User role         (default: "user" | options: "user", "admin", "editor")

    EXAMPLE:
      username = "john_doe", email = "john@example.com", role = "admin"
      →  ✅ User 'john_doe' created with role 'admin'.

    NEXT STEPS:
      → Use get_user to view the profile
      → Use user://{username} in Resources tab

    TRY IT: Fill in username and email, then click Run Tool.
    """
    if username in users:
        return f"⚠️ User '{username}' already exists. Choose a different username."
    users[username] = {
        "email": email,
        "role": role,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    return f"✅ User '{username}' created with role '{role}'."


@mcp.tool()
def get_user(username: str) -> dict | str:
    """
    🔍 GET USER DETAILS

    Retrieves full profile information for a registered user.

    INPUTS:
      username → The exact username (e.g. "john_doe")

    EXAMPLE:
      username = "john_doe"
      →  { username: "john_doe", email: "john@example.com", role: "admin", created_at: "..." }

    PREREQUISITE:
      → First create a user using create_user tool

    TRY IT: Enter the username and click Run Tool.
    """
    user = users.get(username)
    if not user:
        return f"❌ User '{username}' not found. Use list_users to see all users."
    return {"username": username, **user}


@mcp.tool()
def list_users() -> list[str]:
    """
    👥 LIST ALL USERS

    Returns a list of all registered usernames.

    INPUTS:
      (none required)

    EXAMPLE:
      →  ["john_doe", "alice", "bob_admin"]
      →  ["📭 No users yet. Use create_user to add one."]

    TRY IT: Just click Run Tool — no inputs needed.
    """
    return list(users.keys()) if users else ["📭 No users yet. Use create_user to add one."]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🛠️ UTILITY TOOLS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@mcp.tool()
def current_datetime() -> str:
    """
    🕐 GET CURRENT DATE & TIME

    Returns the current server date and time.

    INPUTS:
      (none required)

    EXAMPLE:
      →  "2024-01-15 14:30:45"

    TRY IT: Just click Run Tool — no inputs needed.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@mcp.tool()
def calculate_bmi(weight_kg: float, height_m: float) -> dict:
    """
    ⚖️ CALCULATE BODY MASS INDEX (BMI)

    Calculates BMI and returns the health category.

    INPUTS:
      weight_kg → Weight in kilograms  (e.g. 70)
      height_m  → Height in meters     (e.g. 1.75)

    BMI CATEGORIES:
      Below 18.5  →  Underweight
      18.5 – 24.9 →  Normal weight ✅
      25.0 – 29.9 →  Overweight
      30.0+       →  Obese

    EXAMPLE:
      weight_kg = 70, height_m = 1.75
      →  { bmi: 22.86, category: "Normal weight ✅" }

    TRY IT: Enter your weight and height, then click Run Tool.
    """
    if height_m <= 0:
        return {"error": "❌ Height must be greater than 0."}
    bmi = round(weight_kg / (height_m ** 2), 2)
    if bmi < 18.5:
        category = "Underweight 🔵"
    elif bmi < 25:
        category = "Normal weight ✅"
    elif bmi < 30:
        category = "Overweight 🟡"
    else:
        category = "Obese 🔴"
    return {"bmi": bmi, "category": category}


@mcp.tool()
def convert_temperature(value: float, from_unit: str = "celsius") -> dict:
    """
    🌡️ CONVERT TEMPERATURE

    Converts temperature between Celsius, Fahrenheit, and Kelvin.

    INPUTS:
      value     → Temperature value   (e.g. 100)
      from_unit → Unit to convert from (default: "celsius")
                  Options: "celsius" | "fahrenheit" | "kelvin"

    EXAMPLES:
      value = 100, from_unit = "celsius"
      →  { celsius: 100, fahrenheit: 212.0, kelvin: 373.15 }

      value = 32, from_unit = "fahrenheit"
      →  { celsius: 0.0, fahrenheit: 32, kelvin: 273.15 }

    TRY IT: Enter a temperature value and unit, then click Run Tool.
    """
    unit = from_unit.lower()
    if unit == "celsius":
        c = value
    elif unit == "fahrenheit":
        c = (value - 32) * 5 / 9
    elif unit == "kelvin":
        c = value - 273.15
    else:
        return {"error": f"❌ Unknown unit '{from_unit}'. Use: celsius, fahrenheit, or kelvin."}

    return {
        "celsius":    round(c, 2),
        "fahrenheit": round((c * 9 / 5) + 32, 2),
        "kelvin":     round(c + 273.15, 2),
    }


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦 RESOURCES
# (Access via the "Resources" tab → "List Templates")
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@mcp.resource("note://{title}")
def read_note_resource(title: str) -> str:
    """
    📝 READ NOTE RESOURCE

    Access a saved note directly as a resource.

    HOW TO USE:
      1. Go to Resources tab
      2. Click List Templates
      3. Select note://{title}
      4. Enter the note title (e.g. shopping-list)
      5. Click Read Resource

    PREREQUISITE: Create a note first using the create_note tool.
    """
    content = notes.get(title)
    if not content:
        return f"❌ Note '{title}' not found.\n\nTip: Use the create_note tool first, then come back here."
    return f"📝 NOTE: {title}\n{'─' * 40}\n{content}"


@mcp.resource("user://{username}")
def read_user_resource(username: str) -> str:
    """
    👤 READ USER PROFILE RESOURCE

    Access a user's full profile as a resource.

    HOW TO USE:
      1. Go to Resources tab
      2. Click List Templates
      3. Select user://{username}
      4. Enter the username (e.g. john_doe)
      5. Click Read Resource

    PREREQUISITE: Create a user first using the create_user tool.
    """
    user = users.get(username)
    if not user:
        return f"❌ User '{username}' not found.\n\nTip: Use the create_user tool first, then come back here."
    return (
        f"👤 USER PROFILE\n{'─' * 40}\n"
        f"Username : {username}\n"
        f"Email    : {user['email']}\n"
        f"Role     : {user['role']}\n"
        f"Created  : {user['created_at']}"
    )


@mcp.resource("server://info")
def server_info() -> str:
    """
    🖥️ SERVER INFORMATION

    Displays live server statistics and status.

    HOW TO USE:
      1. Go to Resources tab
      2. Click List Templates
      3. Select server://info
      4. Click Read Resource (no variable needed)
    """
    return (
        f"🚀 SERVER STATUS\n{'─' * 40}\n"
        f"Name         : ProfessionalServer\n"
        f"Status       : ✅ Online\n"
        f"Total Notes  : {len(notes)}\n"
        f"Total Users  : {len(users)}\n"
        f"Server Time  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"{'─' * 40}\n"
        f"Available Resources:\n"
        f"  📝 note://{{title}}       → Read a note\n"
        f"  👤 user://{{username}}    → Read a user profile\n"
        f"  🖥️  server://info         → This page"
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 💬 PROMPTS
# (Access via the "Prompts" tab → "List Prompts")
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@mcp.prompt()
def summarize_note(title: str) -> str:
    """
    📋 SUMMARIZE A NOTE (AI Prompt)

    Generates a ready-to-use AI prompt to summarize a saved note.

    INPUTS:
      title → The note title to summarize (e.g. "meeting-notes")

    HOW TO USE:
      1. First create a note using create_note tool
      2. Go to Prompts tab → List Prompts
      3. Select summarize_note
      4. Enter the note title
      5. Click Get Prompt
      6. Copy the generated prompt and paste it into any AI chat

    PREREQUISITE: Create a note first using the create_note tool.
    """
    content = notes.get(title, f"[Note '{title}' not found — create it first using create_note]")
    return (
        f"Please read the following note and provide a clear, concise summary "
        f"in 2-3 sentences.\n\n"
        f"Note Title: {title}\n"
        f"{'─' * 40}\n"
        f"{content}\n"
        f"{'─' * 40}\n\n"
        f"Summary:"
    )


@mcp.prompt()
def introduce_user(username: str) -> str:
    """
    🎤 INTRODUCE A USER (AI Prompt)

    Generates a ready-to-use AI prompt to write a professional introduction for a user.

    INPUTS:
      username → The username to introduce (e.g. "john_doe")

    HOW TO USE:
      1. First create a user using create_user tool
      2. Go to Prompts tab → List Prompts
      3. Select introduce_user
      4. Enter the username
      5. Click Get Prompt
      6. Copy the generated prompt and paste it into any AI chat

    PREREQUISITE: Create a user first using the create_user tool.
    """
    user = users.get(username)
    if not user:
        return f"[User '{username}' not found — create them first using create_user tool]"
    return (
        f"Write a short, professional introduction (2-3 sentences) for the following person:\n\n"
        f"Name     : {username}\n"
        f"Email    : {user['email']}\n"
        f"Role     : {user['role']}\n"
        f"Member since: {user['created_at']}\n\n"
        f"Introduction:"
    )
