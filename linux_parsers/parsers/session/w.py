import re

from typing import Dict, Any


def parse_w(command_output: str) -> Dict[str, Any]:
    """Parse `w` command output."""
    metadata_pattern = re.compile(
        r"(?P<time>\S+)\D+(?P<uptime>\S+),\s+(?P<users>\d+)\D+"
        r"(?P<load1>\S+),\s+(?P<load2>\S+),\s+(?P<load3>\S+)"
    )
    record_pattern = re.compile(
        r"^(?P<user>\S+)\s+(?P<tty>\S+)\s+(?P<from>\S+)\s+(?P<login>\S+)\s+"
        r"(?P<idle>\S+)\s+(?P<jcpu>\S+)\s+(?P<pcpu>\S+)\s+(?P<command>.+)$",
        re.MULTILINE,
    )
    parsed_output = {"records": []}
    lines = command_output.splitlines()
    while lines:
        line = lines.pop(0)
        if "load average" in line:
            parsed_output["metadata"] = metadata_pattern.search(line).groupdict()
        elif line.startswith("USER") and "LOGIN@" in line:
            continue
        else:
            regex_result = record_pattern.search(line)
            if regex_result:
                parsed_output["records"].append(regex_result.groupdict())
    return parsed_output
