import re
from typing import Optional, Dict, Any


def parse_proc_version(command_output: str) -> Optional[Dict[str, Any]]:
    """Parse `/proc/version` file output."""
    pattern = re.compile(
        r"^Linux version\s+(?P<kernel_version>\S+)\s+"
        r"\((?P<builder>[^)]+)\)\s+"
        r"\((?P<compiler>[^)]+)\)"
        r"(?:,\s+(?P<linker>[^)]+))?\s+"
        r"(?P<build_info>#\S+)\s+"
        r"(?P<build_type>\S+)\s+"
        r"(?P<build_date>.+)$"
    )
    regex_result = re.search(pattern, command_output)
    return regex_result.groupdict() if regex_result else None
