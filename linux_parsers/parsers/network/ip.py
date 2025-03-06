import re
from typing import Any, List, Dict

from linux_parsers.parsers.exceptions import UnexpectedParseException


def parse_ip_a(command_output: str) -> list[Any] | None:
    """parse `ip a` command output"""
    interfaces_names = re.findall(r'^\d:\s(.+):', command_output, flags=re.MULTILINE)
    interfaces = re.split(r'^\d:\s.+:', command_output, flags=re.MULTILINE)
    interfaces.pop(0)  # get rid of first item (its always empty)

    if len(interfaces_names) != len(interfaces):
        UnexpectedParseException(f"len(interfaces_names) != len(interfaces)")

    if not interfaces:
        return

    parsed_interfaces = list()

    for i in range(len(interfaces_names)):
        interface_lines: list[str] = interfaces[i].splitlines()
        flags_info = _parse_flags(interface_lines.pop(0).strip())
        link_layer_info = _parse_link_layer_info(interface_lines.pop(0).strip())
        inets = list()
        while interface_lines:
            inet_line = interface_lines.pop(0).strip()
            inet_flags_line = interface_lines.pop(0).strip()
            inets.append(_parse_inet_line(inet_line) | _parse_lease_time(inet_flags_line))
        parsed_interfaces.append({
            'info': flags_info,
            'link': link_layer_info,
            'inets': inets,
        })
        return parsed_interfaces


def _parse_inet_line(inet_line: str) -> dict:
    """
    parse inet line (e.g: inet 127.0.0.1/8 scope host lo)
    """
    inet_pattern = (
        r"(?P<type>inet(?:6|))"
        r"\s(?P<ip>\S+)"
        r"(?:\sbrd\s(?P<brd>\S+))?\s+"
        r"scope\s(?P<scope>.+)"
    )
    regex_result = re.match(inet_pattern, inet_line)
    return regex_result.groupdict() if regex_result else {}


def _parse_lease_time(inet_flags_line: str) -> dict:
    """
    parse the valid_lft (Valid Lifetime) and preferred_lft (Preferred Lifetime) fields.
    """
    inet_flags_pattern = (
        r"valid_lft\s(?P<valid_lft>.+)\s"
        r"preferred_lft\s(?P<preferred_lft>.+)"
    )
    regex_result = re.match(inet_flags_pattern, inet_flags_line)
    return regex_result.groupdict() if regex_result else {}


def _parse_flags(flags_info: str) -> dict:
    """
    parse flags info
    (e.g: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000)
    """
    pattern = (
        r"<(?P<flags>.+)>\s+"
        r"mtu\s(?P<mtu>.+)\s"
        r"qdisc\s(?P<qdisc>.+)\s"
        r"state\s(?P<state>.+)\s"
        r"group\s(?P<group>.+)\s"
        r"qlen\s(?P<qlen>.+)"
    )
    regex_result = re.match(pattern, flags_info)
    return regex_result.groupdict() if regex_result else {}


def _parse_link_layer_info(link_layer_info: str) -> dict:
    """parse link layer info (e.g: link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00)"""
    pattern = (
        r"link\/(?P<link>.+)\s"
        r"(?P<ip>.+)\s"
        r"brd\s(?P<brd>.+)"
    )
    regex_result = re.match(pattern, link_layer_info)
    return regex_result.groupdict() if regex_result else {}


def parse_ip_r(command_output: str) -> list[dict[str, str | Any]]:
    """
    parse `ip route` command output.
    """
    route_pattern = re.compile(r"""
        (?P<type>default|blackhole|unreachable|prohibit|broadcast|\d+\.\d+\.\d+\.\d+/\d+)  # Route type or destination
        (?:\s+via\s+(?P<via>\d+\.\d+\.\d+\.\d+))?  # Optional next-hop IP
        (?:\s+dev\s+(?P<dev>\S+))?  # Optional interface (e.g., eth0)
        (?:\s+proto\s+(?P<proto>\S+))?  # Optional protocol (e.g., kernel, static, dhcp)
        (?:\s+scope\s+(?P<scope>\S+))?  # Optional scope (e.g., link)
        (?:\s+src\s+(?P<src>\d+\.\d+\.\d+\.\d+))?  # Optional source IP
        (?:\s+metric\s+(?P<metric>\d+))?  # Optional metric
    """, re.VERBOSE)
    return [match.groupdict() for match in route_pattern.finditer(command_output)]
