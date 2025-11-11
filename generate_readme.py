import os

# === SETTINGS ===
LEVELS = ["easy", "medium", "hard"]
README_FILE = "README.md"
SHOW_EMOJIS = True  # Set to False for plain version

# === EMOJIS ===
EMOJI_MAP = {
    "easy": "🟢",
    "medium": "🟡",
    "hard": "🔴"
} if SHOW_EMOJIS else {key: "" for key in LEVELS}

# === Header ===
readme_header = """# 🧠 LeetCode Solutions

This repository contains my Python, C, and C++ solutions to LeetCode problems, organized by difficulty.

## 📊 Problem Count

"""

# === Body Generator ===
def generate_section(level: str, files: list[str]) -> str:
    if not files:
        return ""

    section = f"\n### {EMOJI_MAP[level]} {level.capitalize()} Problems ({len(files)} solved)\n\n"
    section += "| # | Problem | Language | File |\n"
    section += "|---|----------|-----------|------|\n"

    for file in sorted(files):
        try:
            problem_num, name_raw = file.split("-", 1)
            name_clean = name_raw.replace(".py", "").replace(".c", "").replace(".cpp", "").replace("-", " ").title()
            url_slug = name_raw.replace(".py", "").replace(".c", "").replace(".cpp", "")
            leetcode_url = f"https://leetcode.com/problems/{url_slug}/"
            file_path = f"{level}/{file}"

            # Detect programming language by file extension
            if file.endswith(".py"):
                lang = "Python 🐍"
            elif file.endswith(".c"):
                lang = "C 💻"
            elif file.endswith(".cpp"):
                lang = "C++ ⚙️"
            else:
                lang = "Other"

            section += f"| {problem_num} | [{name_clean}]({leetcode_url}) | {lang} | [{file}]({file_path}) |\n"
        except ValueError:
            continue  # skip improperly named files

    return section


# === Main ===
def main():
    base_dir = os.getcwd()
    level_data = {}

    for level in LEVELS:
        folder_path = os.path.join(base_dir, level)
        if not os.path.exists(folder_path):
            level_data[level] = []
            continue

        # Collect files in supported languages
        code_files = [f for f in os.listdir(folder_path) if f.endswith((".py", ".c", ".cpp"))]
        level_data[level] = code_files

    # Write README.md
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme_header)

        # Summary table
        f.write("| Difficulty | Solved |\n")
        f.write("|------------|--------|\n")
        for level in LEVELS:
            count = len(level_data[level])
            f.write(f"| {level.capitalize()} | {count} |\n")

        # Section per difficulty
        for level in LEVELS:
            section = generate_section(level, level_data[level])
            f.write(section)


if __name__ == "__main__":
    main()
