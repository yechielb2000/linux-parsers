import re

from typing import List, Dict, Any


def parse_etc_gshadow_file(command_output: str) -> List[Dict[str, Any]]:
    """Parse `/etc/gshadow` file."""
    pattern = re.compile(
        r"^(?P<group_name>[^:]+):(?P<encrypted_password>[^:]*):(?P<group_id>\d*):(?P<users>.*)$",
        re.MULTILINE,
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
