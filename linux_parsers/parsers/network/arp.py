import re


def parse_arp(command_output: str) -> list[dict[str, str]]:
    """
    parse arp commands
    `arp -i <interface>`.
    `arp -en`.
    `arp -e`.
    """
    pattern = re.compile(
        r'^(?P<Address>\S+)\b\s+'
        r'(?P<HWtype>\S+)\b\s+'
        r'(?P<HWaddress>\S+)\b\s+'
        r'(?P<FlagsMask>\S+)\b\s+'
        r'(?P<Iface>\S+)$',
        flags=re.MULTILINE
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
