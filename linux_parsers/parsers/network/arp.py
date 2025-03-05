import re


def parse_arp_i(command_output: str) -> list[dict[str, str]]:
    """parse `arp -i <interface>`"""
    pattern = (
        r'^(?P<Address>\S+)\b\s+'
        r'(?P<HWtype>\S+)\b\s+'
        r'(?P<HWaddress>\S+)\b\s+'
        r'(?P<FlagsMask>\S+)\b\s+'
        r'(?P<Iface>\S+)$'
    )
    return [i.groupdict() for i in re.finditer(pattern, command_output, flags=re.MULTILINE)]
