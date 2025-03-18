import re

from typing import Dict, Any


def parse_mpstat(command_output: str) -> Dict[str, Any]:
    """Parse `mpstat -P ALL` command output."""
    metadata_pattern = re.compile(
        r"(?P<os>[\s\S]+)\s\((?P<hostname>.+)\)\s+(?P<execute_date>\d+/\d+/\d+)"
        r"\s+(?P<architecture>\S+)\s+\((?P<available_cpu>\d+).+\)"
    )
    statistics_pattern = re.compile(
        r"(?P<time>\S+\s(?:PM|AM)?)\s+(?P<cpu>\S+)\s+(?P<usr>[\d.]+)\s+(?P<nice>[\d.]+)\s+(?P<sys>[\d.]+)\s+"
        r"(?P<iowait>[\d.]+)\s+(?P<irq>[\d.]+)\s+(?P<soft>[\d.]+)\s+(?P<steal>[\d.]+)\s+(?P<guest>[\d.]+)\s+"
        r"(?P<gnice>[\d.]+)\s+(?P<idle>[\d.]+)"
    )
    lines = [i.strip() for i in command_output.splitlines() if i.strip()]
    parsed_output = metadata_pattern.search(lines.pop(0)).groupdict()
    parsed_output["statistics"] = []
    while lines:
        line = lines.pop(0)
        regex_result = statistics_pattern.search(line)
        if regex_result:
            parsed_output["statistics"].append(regex_result.groupdict())
    return parsed_output
