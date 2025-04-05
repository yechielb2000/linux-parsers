import re
from typing import Dict, Any, List


def parse_ac_p(command_output: str) -> Dict[str, Any]:
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
    pattern = re.compile(r"(?P<date>.+)\b\s+total\s+(?P<total>.+)")
    return [i.groupdict() for i in pattern.finditer(command_output)]
