import shlex
from typing import Optional, Set, Callable, Tuple, Any

from linux_parsers.parsers_registry import PARSER_REGISTRY


def _parse_command_string(command: str) -> Tuple[str, Optional[str], Set[Any]]:
    parts = shlex.split(command)
    binary = parts[0]
    args = parts[1:]

    subcommand = None
    flags = set()

    for arg in args:
        if arg.startswith("--"):
            flags.add(arg)
        elif arg.startswith("-") and len(arg) > 2:
            for ch in arg[1:]:
                flags.add(f"-{ch}")
        elif arg.startswith("-"):
            flags.add(arg)
        elif subcommand is None:
            subcommand = arg

    return binary, subcommand, flags


def _find_matching_parser(binary: str, subcommand: Optional[str], flags: Set[str]) -> Optional[Callable[[str], dict]]:
    candidates = PARSER_REGISTRY.get(binary, [])

    for entry in candidates:
        if entry.get("subcommand_aliases"):
            if subcommand not in entry["subcommand_aliases"]:
                continue

        if entry["must_have"]:
            if not entry["must_have"] == flags:
                continue

        if entry["one_of"]:
            if not entry["one_of"] & flags:
                continue

        return entry["parser"]

    return None


def auto_parse_output(command: str, output: str) -> Optional[dict]:
    binary, subcommand, flags = _parse_command_string(command)
    parser_func = _find_matching_parser(binary, subcommand, flags)

    if parser_func:
        return parser_func(output)

    print(f"No matching parser found for: {command}")
    return None
