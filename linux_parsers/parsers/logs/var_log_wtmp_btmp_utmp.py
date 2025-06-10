"""
Must be tested dynamically. Currently published without any tests.
# TODO: add tests
"""

import struct
from typing import List, Dict, Optional, Tuple, Any

_RECORD_SIZE = 384
_STRUCT_FORMAT = "hi32s4s32s256shhiii4i20s"

_UT_TYPE_MAP = {
    0: "EMPTY",
    1: "RUN_LVL",
    2: "BOOT_TIME",
    3: "NEW_TIME",
    4: "OLD_TIME",
    5: "INIT_PROCESS",
    6: "LOGIN_PROCESS",
    7: "USER_PROCESS",
    8: "DEAD_PROCESS",
    9: "ACCOUNTING",
}


def _parse_records(file_bytes: bytes) -> List[Dict[str, str]]:
    records = []
    for i in range(0, len(file_bytes), _RECORD_SIZE):
        chunk = file_bytes[i : i + _RECORD_SIZE]
        if len(chunk) < _RECORD_SIZE:
            break

        fields = struct.unpack(_STRUCT_FORMAT, chunk)
        record = {
            "type": _UT_TYPE_MAP.get(fields[0], f"UNKNOWN({fields[0]})"),
            "pid": fields[1],
            "line": fields[2].split(b"\x00", 1)[0].decode("utf-8", errors="ignore"),
            "id": fields[3].split(b"\x00", 1)[0].decode("utf-8", errors="ignore"),
            "user": fields[4].split(b"\x00", 1)[0].decode("utf-8", errors="ignore"),
            "host": fields[5].split(b"\x00", 1)[0].decode("utf-8", errors="ignore"),
            "exit_status": {
                "termination": fields[6],
                "exit": fields[7],
            },
            "session": fields[8],
            "timestamp": fields[9],
            "ip": _ip_from_fields(fields[11:15]),
        }
        records.append(record)
    return records


def _ip_from_fields(addr_v6_fields: Tuple[Any, ...]) -> Optional[str]:
    if all(x == 0 for x in addr_v6_fields):
        return None
    ipv4 = addr_v6_fields[0]
    return ".".join(str((ipv4 >> (8 * i)) & 0xFF) for i in range(4))


def parse_var_log_utmp(file_bytes: bytes):
    return _parse_records(file_bytes)


def parse_var_log_wtmp(file_bytes: bytes):
    return _parse_records(file_bytes)


def parse_var_log_btmp(file_bytes: bytes):
    return _parse_records(file_bytes)
