import os
import re
from datetime import datetime

# Paths
DOCS_DIR = "docs"
SOLUTIONS_DIR = "solutions"
PROGRESS_FILE = os.path.join(DOCS_DIR, "progress.md")


def get_solved_problems():
    """Scans the solutions directory and returns a dictionary of {problem_id: relative_path}"""
    solved = {}
    if not os.path.exists(SOLUTIONS_DIR):
        return solved

    for root, dirs, files in os.walk(SOLUTIONS_DIR):
        for file in files:
            if file.endswith(".cpp"):
                # Expected format: LC_0001_Two_Sum.cpp
                match = re.search(r"LC_0(\d+)_", file) or re.search(r"LC_(\d+)_", file)
                if match:
                    problem_id = int(match.group(1))
                    # Create relative path from docs/ folder to solutions/ folder
                    rel_path = f"../{os.path.relpath(os.path.join(root, file), start=DOCS_DIR).replace(os.sep, '/')}"
                    solved[problem_id] = rel_path
    return solved


def update_markdown():
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    solved_problems = get_solved_problems()

    stats = {"Total": 0, "Easy": 0, "Medium": 0, "Hard": 0}

    # 1. Update the Problem Tracker Table
    lines = content.split("\n")
    new_lines = []
    in_table = False

    for line in lines:
        # Detect table rows by checking if it starts with | and has a number in the first column
        row_match = re.match(
            r"\|\s*(\d+)\s*\|(.*)\|([^|]+)\|\s*([^|]+)\|\s*(.+)\|\s*(.+)\|", line
        )

        if row_match:
            problem_id = int(row_match.group(1))
            problem_name = row_match.group(2)
            pattern = row_match.group(3)
            difficulty_raw = row_match.group(4)

            # Determine difficulty for stats
            if "Easy" in difficulty_raw:
                difficulty = "Easy"
            elif "Medium" in difficulty_raw:
                difficulty = "Medium"
            elif "Hard" in difficulty_raw:
                difficulty = "Hard"
            else:
                difficulty = "Unknown"

            if problem_id in solved_problems:
                stats["Total"] += 1
                if difficulty in stats:
                    stats[difficulty] += 1

                status = "✅"
                solution_link = f"[✔️]({solved_problems[problem_id]})"

                # Rebuild the line
                new_line = f"| {problem_id} |{problem_name}|{pattern}| {difficulty_raw} | {status} | {solution_link} |"
                new_lines.append(new_line)
            else:
                # Keep as not solved
                status = "⬜"
                solution_link = "❌"
                new_line = f"| {problem_id} |{problem_name}|{pattern}| {difficulty_raw} | {status} | {solution_link} |"
                new_lines.append(new_line)
        else:
            new_lines.append(line)

    updated_content = "\n".join(new_lines)

    # 2. Update the Statistics Section
    today = datetime.now().strftime("%Y-%m-%d")
    stats_text = f"""| Metric                |      Value     |
| --------------------- | :------------: |
| Total Problems Solved |      **{stats['Total']}** |
| Easy                  |      **{stats['Easy']}** |
| Medium                |      **{stats['Medium']}** |
| Hard                  |      **{stats['Hard']}** |
| Last Updated          | **{today}** |
"""

    # Replace stats using regex
    updated_content = re.sub(r".*?", stats_text, updated_content, flags=re.DOTALL)

    # Replace bottom Last Updated if exists
    updated_content = re.sub(
        r"\*\*Last Updated:\*\* .*", f"**Last Updated:** {today}", updated_content
    )

    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"✅ Successfully updated {PROGRESS_FILE}. Total solved: {stats['Total']}")


if __name__ == "__main__":
    update_markdown()
