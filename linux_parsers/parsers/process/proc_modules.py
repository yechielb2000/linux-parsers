from typing import List, Dict, Any


def parse_proc_modules(command_output: str) -> List[Dict[str, Any]]:
    """Parse `/proc/modules` file."""
    parsed_command = []
    for line in command_output.splitlines():
        line_block = line.strip().split()
        if len(line_block) >= 6:
            module = {
                "name": line_block[0],
                "size": int(line_block[1]),
                "instances": int(line_block[2]),
                "dependencies": [i for i in line_block[3].split(",") if i] if line_block[3] != "-" else [],
                "state": line_block[4],
                "address": line_block[5],
            }
            parsed_command.append(module)
    return parsed_command
