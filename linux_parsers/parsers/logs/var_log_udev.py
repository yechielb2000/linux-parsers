import re
from typing import List, Dict


def parse_var_log_udev(command_output: str) -> List[Dict[str, str]]:
    """Parse content of `/var/log/udev` lgn file."""
    entries = []
    lines = command_output.strip().splitlines()

    current_entry = {}
    for line in lines:
        line = line.strip()
        if line.startswith("UDEV"):
            if current_entry:
                entries.append(current_entry)
                current_entry = {}
            match = re.match(r"UDEV\s+\[(.*?)\]\s+(\w+)\s+(.*?)\s+\((.*?)\)", line)
            if match:
                current_entry["timestamp"] = match.group(1)
                current_entry["action"] = match.group(2)
                current_entry["devpath"] = match.group(3)
                current_entry["subsystem"] = match.group(4)
        elif "=" in line:
            key, value = line.split("=", 1)
            current_entry[key] = value
    if current_entry:
        entries.append(current_entry)
    return entries
