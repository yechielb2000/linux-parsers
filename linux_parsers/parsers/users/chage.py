from typing import Dict


def parse_chage_l(command_output: str) -> Dict[str, str]:
    """Parse `chage -l <username>` command output"""
    parsed_output = {}
    for line in [i.strip() for i in command_output.splitlines() if i.strip()]:
        key, value = [i.strip() for i in line.split(":")]
        parsed_output[key] = value
    return parsed_output
