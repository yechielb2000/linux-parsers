import re
from typing import Dict, List


def parse_proc_devices(command_output: str) -> Dict[str, List[Dict[str, str]]]:
    record_pattern = re.compile(r"\s*(?P<major_num>\S+)\s+(?P<name>.+)")
    lines = command_output.strip().splitlines()
    parsed_command = {"character_devices": [], "block_devices": []}
    current_device_type = None
    for line in lines:
        if line.startswith("Character devices:"):
            current_device_type = "character_devices"
            continue
        if line.startswith("Block devices:"):
            current_device_type = "block_devices"
            continue
        match = record_pattern.search(line)
        if match:
            parsed_command[current_device_type].append(match.groupdict())
    return parsed_command
