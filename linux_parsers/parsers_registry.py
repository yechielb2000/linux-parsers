from linux_parsers.parsers.network import ss, arp, ip, ping, ufw

FILE_READERS = {"cat", "head", "tail", "less", "more"}

PARSER_REGISTRY = {
    "ss": [
        {
            "must_have": {"s"},
            "one_of": [],
            "func": ss.parse_ss_s,
        },
        {
            "must_have": {"t", "u", "l", "n", "a", "p"},
            "one_of": [],
            "func": ss.parse_ss_tulnap,
        },
    ],
    "arp": [
        {
            "must_have": set(),
            "one_of": [],
            "func": arp.parse_arp,
        }
    ],
    "ip": [
        {
            "subcommand_aliases": ["a", "addr", "address"],
            "must_have": set(),
            "one_of": [],
            "func": ip.parse_ip_a,
        },
        {
            "subcommand_aliases": ["n"],
            "must_have": set(),
            "one_of": [],
            "func": ip.parse_ip_n,
        },
        {
            "subcommand_aliases": ["r", "route"],
            "must_have": set(),
            "one_of": [],
            "func": ip.parse_ip_r,
        },
    ],
    "ping": [
        {
            "must_have": set(),
            "one_of": [],
            "func": ping.parse_ping,
        }
    ],
    "ufw": [
        {
            "subcommand_aliases": ["status"],
            "must_have": set(),
            "one_of": [],
            "func": ufw.parse_ufw_status,
        },
        {
            "subcommand_aliases": ["app list"],  # TODO: check if this works
            "must_have": set(),
            "one_of": [],
            "func": ufw.parse_ufw_app_list,
        },
    ],
}
