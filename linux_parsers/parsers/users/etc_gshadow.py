import re


def parse_etc_gshadow_file(command_output: str) -> list[dict[str, any]]:
    """Parse `/etc/gshadow` file."""
    pattern = re.compile(
        r'^(?P<group_name>[^:]+):(?P<encrypted_password>[^:]*):(?P<group_id>\d*):(?P<users>.*)$',
        re.MULTILINE
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
