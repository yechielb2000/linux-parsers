import re


def parse_vmstat(command_output: str) -> list[dict[str, dict]]:
    """Parse `vmstat` command output."""
    pattern = re.compile(
        r"\s+(?P<r>\d+)\s+(?P<b>\d+)\s+(?P<swpd>\d+)\s+(?P<free>\d+)\s+(?P<buff>\d+)\s+"
        r"(?P<cache>\d+)\s+(?P<si>\d+)\s+(?P<so>\d+)\s+(?P<bi>\d+)\s+(?P<bo>\d+)\s+"
        r"(?P<in>\d+)\s+(?P<cs>\d+)\s+(?P<us>\d+)\s+(?P<sy>\d+)\s+(?P<id>\d+)\s+"
        r"(?P<wa>\d+)\s+(?P<st>\d+)\s+(?P<gu>\d+)"
    )
    parsed_command = []
    for record in pattern.finditer(command_output):
        record = record.groupdict()
        parsed_command.append({
            'procs': {
                'r': record['r'],
                'b': record['b']
            },
            'memory': {
                'swpd': record['swpd'],
                'free': record['free'],
                'buff': record['buff'],
                'cache': record['cache']
            },
            'swap': {
                'si': record['si'],
                'so': record['so']
            },
            'io': {
                'bi': record['bi'],
                'bo': record['bo']
            },
            'system': {
                'in': record['in'],
                'cs': record['cs']
            },
            'cpu': {
                'us': record['us'],
                'sy': record['sy'],
                'id': record['id'],
                'wa': record['wa'],
                'st': record['st'],
                'gu': record['gu']
            },
        })
    return parsed_command
