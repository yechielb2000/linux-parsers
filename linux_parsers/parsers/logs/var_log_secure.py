import re
from typing import List, Dict


def parse_var_log_secure(command_output: str) -> List[Dict[str, str]]:
    """
    Parse `/var/logs/secure` file output.
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
