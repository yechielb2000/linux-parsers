import re
from typing import List, Dict


def _basic_log_parser(command_output: str) -> List[Dict[str, str]]:
    """
    This parser is for most common distributions.
    If the configuration of the logfile was changed it will probably won't be able to parse it.
    """
    pattern = re.compile(
        r"(?P<timestamp>\w{3}\s\d+\s\d+:\d+:\d+)\s+"
        r"(?P<hostname>\S+)\s+"
        r"(?P<process>[^:]+):\s+"
        r"(?P<message>.+)"
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]


__all__ = ["_basic_log_parser"]
