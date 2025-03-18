from typing import Dict


def parse_etc_os_release_file(command_output: str) -> Dict[str, str]:
    """Parse `/etc/os-release` file."""
    parsed_output = {}
    lines = command_output.splitlines()
    for line in lines:
        key, value = line.split("=", 1)
        parsed_output[key] = value.replace('"', "").strip()
    return parsed_output
