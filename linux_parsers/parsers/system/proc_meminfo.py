from typing import Dict


def parse_proc_meminfo_file(command_output: str) -> Dict[str, str]:
    """Parse `/proc/meminfo` file"""
    parsed_output = {}
    lines = command_output.splitlines()
    for line in lines:
        if not line:
            continue
        key, value = line.split(":")
        parsed_output[key.strip()] = value.strip()
    return parsed_output
