import random
from datetime import datetime

mantras = [
    "Optimizing REST API endpoints on Render.",
    "Refactoring Firebase JWT authentication middleware.",
    "Training local datasets to minimize LLM hallucinations.",
    "Perfecting UI responsiveness with precise CSS layout systems.",
    "Analyzing normalized MySQL relational schemas for society databases.",
    "Debugging Node.js Express middleware chain.",
    "Writing clean Firestore security rules for role-based access.",
    "Exploring Gemini API capabilities for smarter chatbot responses.",
    "Building GitHub Actions workflows to automate deployments.",
    "Designing RESTful API contracts with proper status codes.",
]

games = ["Detroit: Become Human", "Life is Strange 2", "Portal 2"]
anime = ["One Piece", "Demon Slayer"]


def generate_terminal():
    current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    selected_mantra = random.choice(mantras)
    selected_game = random.choice(games)
    selected_anime = random.choice(anime)

    terminal_template = f"""
```bash
$ init --profile meet0411
[INFO] Synchronizing system logs...
[INFO] Active Environment: Vidyavardhini's College of Engineering & Technology
[INFO] Last Cron Heartbeat: {current_time}

>> CURRENT_FOCUS : {selected_mantra}
>> HARDWARE      : Dell i3-6006U // 4GB RAM // Custom Circuit Tinker Mode [ACTIVE]
>> MEDIA_STREAM  : Compiling episodes of {selected_anime} // Playing {selected_game}
>> SYSTEM_STATUS : Stable. Code. Learn. Build. Repeat.
```
"""
    return terminal_template


def update_readme():
    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()

    start_tag = "<!--DYNAMIC_TERMINAL_START-->"
    end_tag = "<!--DYNAMIC_TERMINAL_END-->"

    if start_tag in content and end_tag in content:
        start_idx = content.find(start_tag) + len(start_tag)
        end_idx = content.find(end_tag)

        new_terminal_content = generate_terminal()
        updated_content = (
            content[:start_idx]
            + "\n"
            + new_terminal_content
            + "\n"
            + content[end_idx:]
        )

        with open("README.md", "w", encoding="utf-8") as file:
            file.write(updated_content)
        print("README terminal log successfully updated!")
    else:
        print("Error: Automation tags not found in README.md")


if __name__ == "__main__":
    update_readme()
