from typing import Dict


def parse_etc_systemd_file_conf(command_output: str) -> Dict[str, Dict[str, str]]:
    """Parse any `/etc/systemd/*.conf` output files."""
    lines = command_output.splitlines()
    parsed_output = {}
    current_parent_key = None
    for line in lines:
        if line:
            if line.startswith("["):
                current_parent_key = line.strip("[]")
                parsed_output[current_parent_key] = {}
            elif current_parent_key and not line.startswith("#"):
                key, value = line.split("=", 1)
                parsed_output[current_parent_key][key] = value.strip()
    return parsed_output
