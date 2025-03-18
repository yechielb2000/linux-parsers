from typing import Dict


def parse_useradd_D(command_output: str) -> Dict[str, str]:
    """Parse `useradd -D` command output."""
    parsed_output = {}
    for line in [i.strip() for i in command_output.splitlines() if i.strip()]:
        key, value = line.split("=")
        parsed_output[key] = value
    return parsed_output
