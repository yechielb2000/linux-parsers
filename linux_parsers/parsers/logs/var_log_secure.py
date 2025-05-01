from typing import List, Dict

from linux_parsers.parsers.logs._basic_log_parser import _basic_log_parser


def parse_var_log_secure(command_output: str) -> List[Dict[str, str]]:
    """Parse `/var/logs/secure` file output."""
    return _basic_log_parser(command_output)
