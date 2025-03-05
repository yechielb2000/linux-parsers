import re


def parse_arp(command_output: str) -> list[dict[str, str]]:
    """
    parse arp commands
    `arp -i <interface>`.
    `arp -en`.
    `arp -e`.
    """
    pattern = (
        r'^(?P<Address>\S+)\b\s+'
        r'(?P<HWtype>\S+)\b\s+'
        r'(?P<HWaddress>\S+)\b\s+'
        r'(?P<FlagsMask>\S+)\b\s+'
        r'(?P<Iface>\S+)$'
    )
    return [i.groupdict() for i in re.finditer(pattern, command_output, flags=re.MULTILINE)]
