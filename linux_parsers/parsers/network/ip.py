import re
from typing import Any, Dict, List


def parse_ip_a(command_output: str) -> Dict[str, Dict[str, Any]]:
    """Parse `ip a` command output."""
    link_pattern = re.compile("link/(?P<link>.+)\s(?P<ip>.+)\sbrd\s(?P<brd>.+)")
    lease_time_pattern = re.compile("valid_lft\s(?P<valid_lft>\S+)\spreferred_lft\s(?P<preferred_lft>\S+)")
    ip_pattern = re.compile("(?P<type>inet6?)\s(?P<ip>\S+)(?:\sbrd\s(?P<brd>\S+))?\s+scope\s(?P<scope>.+)")
    interface_data = re.compile(
        "(?P<index>\d):\s"
        "(?P<iface>\S+):\s"
        "<(?P<flags>[^>]+)>\s"
        "mtu\s(?P<mtu>\d+)\s"
        "qdisc\s(?P<qdisc>\S+)\s"
        "state\s(?P<state>\S+)\s"
        "group\s(?P<group>\S+)"
        "(?:\sqlen\s(?P<qlen>\d+))?"
    )
    interfaces = {}
    blocks = re.split(r"\n(?=\d+:)", command_output.strip())  # Split on lines that start with a digit

    for block in blocks:
        lines: List[str] = [i.strip() for i in block.splitlines()]
        iface_header = lines.pop(0)
        iface_data = interface_data.search(iface_header).groupdict()
        iface_index = iface_data["index"]
        interfaces[iface_index] = iface_data
        interfaces[iface_index]["addresses"] = []
        if lines and lines[0].startswith("link/"):
            regex_result = link_pattern.search(lines.pop(0))
            interfaces[iface_index]["link"] = regex_result.groupdict() if regex_result else {}
        while lines:
            line = lines.pop(0)
            if line.startswith("inet"):
                regex_result = ip_pattern.search(line)
                inet = regex_result.groupdict() if regex_result else {}
                if lines and lines[0].startswith("valid_lft"):
                    regex_result = lease_time_pattern.search(lines.pop(0))
                    inet.update(regex_result.groupdict() if regex_result else {})
                interfaces[iface_index]["addresses"].append(inet)
    return interfaces


def parse_ip_r(command_output: str) -> List[Dict[str, Any]]:
    """parse `ip route` command output."""
    pattern = re.compile(
        r"""
        (?P<type>default|blackhole|unreachable|prohibit|broadcast|\d+\.\d+\.\d+\.\d+/\d+)  # Route type or destination
        (?:\s+via\s+(?P<via>\d+\.\d+\.\d+\.\d+))?  # Optional next-hop IP
        (?:\s+dev\s+(?P<dev>\S+))?  # Optional interface (e.g., eth0)
        (?:\s+proto\s+(?P<proto>\S+))?  # Optional protocol (e.g., kernel, static, dhcp)
        (?:\s+scope\s+(?P<scope>\S+))?  # Optional scope (e.g., link)
        (?:\s+src\s+(?P<src>\d+\.\d+\.\d+\.\d+))?  # Optional source IP
        (?:\s+metric\s+(?P<metric>\d+))?  # Optional metric
    """,
        re.VERBOSE,
    )
    return [match.groupdict() for match in pattern.finditer(command_output)]


def parse_ip_n(command_output: str) -> List[Dict[str, Any]]:
    """parse `ip n` command output."""
    pattern = re.compile(
        r"""
        (?P<ip>(?:\d{1,3}\.){3}\d{1,3} | [a-fA-F0-9:]+)  # IPv4 or IPv6 address
        \s+dev\s+(?P<dev>\S+)  # Device/interface name
        (?:\s+lladdr\s+(?P<lladdr>(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}))?  # Optional MAC address
        \s+(?P<state>\S+)  # Neighbor state
    """,
        flags=re.VERBOSE,
    )
    return [match.groupdict() for match in pattern.finditer(command_output)]
