import re

from typing import List, Dict, Any


def parse_etc_group_file(command_output: str) -> List[Dict[str, Any]]:
    """Parse `/etc/group` file output."""
    pattern = re.compile(
        r"^(?P<group_name>[^:]+):(?P<password>[^:]*):(?P<gid>\d+):(?P<members>[^:]*)$",
        re.MULTILINE,
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
