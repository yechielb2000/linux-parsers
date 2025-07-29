from typing import List, Dict, Any


def parse_lsmod(command_output: str) -> List[Dict[str, Any]]:
    """Parse `lsmod` command output."""
    lines = command_output.strip().splitlines()
    modules = []

    for line in lines[1:]:
        parts = line.split()
        if len(parts) >= 3:
            module = {
                "name": parts[0],
                "size": int(parts[1]),
                "used_by_count": int(parts[2]),
                "used_by_modules": parts[3].split(",") if len(parts) > 3 else [],
            }
            modules.append(module)
    return modules
