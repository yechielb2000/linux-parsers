import re
from typing import Dict, Any, List


def parse_ac_p(command_output: str) -> Dict[str, Any]:
    """Parse `ac -p` command output."""
    user_data_pattern = re.compile(r"\s*(?P<user>\S+)\s+(?P<time>[\d.]+)")
    parsed_output = {"users": [], "total": None}
    lines = [i.strip() for i in command_output.splitlines() if i.strip()]
    while lines:
        line = lines.pop(0)
        if line.startswith("total"):
            parsed_output["total"] = line.split()[1].strip()
            continue
        regex_result = user_data_pattern.search(line)
        if regex_result:
            parsed_output["users"].append(regex_result.groupdict())
    return parsed_output


def parse_ac_d(command_output: str) -> List[Dict[str, Any]]:
    """Parse `ac -d` command output."""
    pattern = re.compile(r"(?P<date>.+)\b\s+total\s+(?P<total>.+)")
    return [i.groupdict() for i in pattern.finditer(command_output)]


def parse_ac_pd(command_output: str):
    """Parse `ac -pd` command output."""
    parsed_output = {}
    current_date = None

    split_dates_pattern = re.compile(r"([A-Z][a-z]{2} \d{2}):")
    date_fields_pattern = re.compile(r"\s+(\S+)\s+([\d.]+)")
    for line in command_output.strip().splitlines():
        if date := split_dates_pattern.search(line):
            current_date = date.group(1)
            parsed_output[current_date] = {}
        elif current_date and (regex_result := date_fields_pattern.search(line)):
            key, value = regex_result.groups()
            parsed_output[current_date][key] = value
    return parsed_output
