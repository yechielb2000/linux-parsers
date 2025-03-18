from typing import Dict, List


def parse_etc_resolve_conf_file(command_output: str) -> Dict[str, List[str]]:
    """Parse `/etc/resolve.conf` file."""

    lines = command_output.splitlines()

    parsed_output = {"nameservers": [], "search_domains": [], "options": []}

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        if line.startswith("nameserver"):
            parsed_output["nameservers"].append(line.split()[1])
        elif line.startswith("search"):
            parsed_output["search_domains"].extend(line.split()[1:])
        elif line.startswith("options"):
            parsed_output["options"].extend(line.split()[1:])

    return parsed_output
