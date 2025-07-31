import os

# Define paths
BASE_DIR = os.getcwd()
LEVELS = ["easy", "medium", "hard"]
README = "README.md"

# Write intro
header = """# LeetCode Solutions

This repository contains my Python solutions to LeetCode problems.

## Problem List by Difficulty
"""

with open(README, "w") as f:
    f.write(header)

    for level in LEVELS:
        path = os.path.join(BASE_DIR, level)
        if not os.path.exists(path):
            continue

        files = sorted([f for f in os.listdir(path) if f.endswith(".py")])
        if not files:
            continue

        f.write(f"\n### {level.capitalize()} Problems\n\n")
        f.write("| # | Problem | File |\n")
        f.write("|---|---------|------|\n")

        for file in files:
            problem_num, name_raw = file.split("-", 1)
            name = name_raw.replace(".py", "").replace("-", " ").title()
            leetcode_url = f"https://leetcode.com/problems/{name_raw.replace('.py','')}/"
            file_path = f"{level}/{file}"
            f.write(f"| {problem_num} | [{name}]({leetcode_url}) | [{file}]({file_path}) |\n")
