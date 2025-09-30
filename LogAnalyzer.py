import re
import os
import json
from datetime import datetime


def read_log(file_path):
    if not os.path.exists(file_path):
        print("Plik nie istnieje!")
        return []
    with open(file_path, "r") as f:
        return f.readlines()


def parse_line(line):
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)"
    match = re.match(pattern, line)
    if match:
        date_str, level, msg = match.groups()
        date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        return {"date": date_str, "level": level, "message": msg}
    return None


def analyze_logs(lines):
    stats = {}
    parsed_lines = []
    for line in lines:
        data = parse_line(line)
        if data:
            parsed_lines.append(data)
            stats[data["level"]] = stats.get(data["level"], 0) + 1
    return parsed_lines, stats


def save_to_json(data, file_name="report.json"):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


log_lines = read_log("log2.txt")
parsed, stats = analyze_logs(log_lines)
print("Statystyki logów:", stats)
save_to_json({"logs": parsed, "stats": stats})
