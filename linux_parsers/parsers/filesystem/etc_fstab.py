import re
from typing import List, Dict, Any


def parse_etc_fstab(command_output: str) -> List[Dict[str, Any]]:
    """Parse `/etc/fstab` file output."""
    mount_record = re.compile(
        r"(?P<device>\S+)\s+"
        r"(?P<mount_point>\S+)\s+"
        r"(?P<filesystem_type>\S+)\s+"
        r"(?P<options>\S+)\s+"
        r"(?P<dump>\d+)\s+"
        r"(?P<pass>\d+)"
    )
    return [i.groupdict() for i in mount_record.finditer(command_output)]
