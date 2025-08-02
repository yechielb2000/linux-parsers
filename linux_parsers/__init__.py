from linux_parsers import parsers
from linux_parsers.command_detection import auto_parse_output
from linux_parsers.parsers_registry import PARSER_REGISTRY

__all__ = [
    "parsers",
    "auto_parse_output",
    "PARSER_REGISTRY",
]
