import re

from typing import List, Dict, Any


def parse_ps_aux(command_output: str) -> List[Dict[str, Any]]:
    """Parse `ps aux`command output."""
    pattern = re.compile(
        "(?P<user>\S+)\s+(?P<pid>\d+)\s+(?P<cpu>\S+)\s+(?P<mem>\S+)\s+(?P<vsz>\d+)\s+(?P<rss>\d+)\s+"
        "(?P<tty>\S+)\s+(?P<stat>\S+)\s+(?P<start>\S+)\s+(?P<time>\S+)\s+(?P<command>.+)"
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]


def parse_ps_ax(command_output: str) -> List[Dict[str, Any]]:
    """Parse `ps -ax` command output."""
    lines = "\n".join([i.strip() for i in command_output.splitlines() if i.strip()])
    pattern = re.compile(r"(?P<pid>\d+)\s+(?P<tty>\S+)\s+(?P<stat>\S+)\s+(?P<time>\S+)\s+(?P<command>.+)")
    return [i.groupdict() for i in pattern.finditer(lines)]


def parse_ps_caweL(command_output: str) -> List[Dict[str, Any]]:
    """Parse `ps -caweL` command output."""
    lines = "\n".join([i.strip() for i in command_output.splitlines() if i.strip()])
    pattern = re.compile(
        r"(?P<pid>\d+)\s+(?P<lwp>\d+)\s+(?P<cls>\S+)\s+"
        r"(?P<pri>\S+)\s+(?P<tty>\S+)\s+(?P<time>\S+)\s+(?P<cmd>.+)"
    )
    return [i.groupdict() for i in pattern.finditer(lines)]


def parse_ps_fadel(command_output: str) -> List[Dict[str, Any]]:
    """Parse `ps -fadel` command output."""
    pattern = re.compile(
        r"(?P<flags>\d+)\s(?P<state>\w+)\s+(?P<uid>\w+)\s+(?P<pid>\d+)\s+(?P<ppid>\d+)\s+"
        r"(?P<cpu>\d+)\s+(?P<priority>\S+)\s+(?P<nice_value>\S+)\s+(?P<mem_addr>\S+)\s+(?P<size>\S+)\s+"
        r"(?P<waiting_channel>\S+)\s+(?P<start_time>\S+)\s+(?P<tty>\S+)\s+(?P<time>\S+)\s+(?P<cmd>.+)"
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
