import re
from typing import Optional, Dict, Any


def parse_proc_version(command_output: str) -> Optional[Dict[str, Any]]:
    """Parse `/proc/version` file output."""
    pattern = re.compile(
        r"^Linux version (?P<kernel_version>\S+)\s+"
        r"\((?P<builder>[^)]+)\)\s+"
        r"\((?P<compiler_and_linker>.+?)\)\s+"
        r"(?P<build_info>#[^\s]+)\s+"
        r"(?P<build_type>\S+)\s+"
        r"(?P<build_date>.+)$"
    )
    parsed_command = {}
    regex_result = pattern.search(command_output)
    if regex_result:
        parsed_command = regex_result.groupdict()

        compiler_linker = parsed_command.pop("compiler_and_linker")
        if ", " in compiler_linker:
            compiler, linker = compiler_linker.split(", ", 1)
            parsed_command["compiler"] = compiler
            parsed_command["linker"] = linker
        else:
            parsed_command["compiler"] = compiler_linker
            parsed_command["linker"] = None
    return parsed_command
