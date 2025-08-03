import subprocess
from typing import Callable, List, Tuple

from linux_parsers.parsers.filesystem import *
from linux_parsers.parsers.network import *

FILESYSTEM_COMMANDS = [
    ("df", parse_df),
    ("ls -la /var", parse_ls),
    ("dpkg -l | head -n 10", parse_dpkg_l),
    ("fdisk -l | head -n 10", parse_fdisk),
    ("stat /etc/passwd", parse_stat),
    ("du -ab /etc", parse_du),
    ("cat /proc/mounts", parse_mount),
]

NETWORK_COMMANDS = [
    ("arp -en", parse_arp),
    ("ip a", parse_ip_a),
    ("ip n", parse_ip_n),
    ("ip route", parse_ip_r),
    ("ss -s", parse_ss_s),
    ("ss -tulnap", parse_ss_tulnap),
    ("ufw status", parse_ufw_status),
    ("ufw app list", parse_ufw_app_list),
    ("ping -c 3 127.0.0.1 ", parse_ping),
    ("cat /etc/resolve.conf", parse_etc_resolve),
    ("iptables -L -n -v", parse_iptables),
    ("netstat -tulpan", parse_netstat),
]


def check_command(command: str, func: Callable):
    command_result = None
    try:
        command_result = subprocess.run(command, capture_output=True, text=True, check=True)
    except Exception as e:
        print(f"Error while running command: {command}.\n\n error: {e}")
    if command_result and command_result.returncode == 0:
        parsed_result = func(command_result.stdout)
        assert parsed_result is not None


def iterate_commands(commands: List[Tuple[str, Callable]]):
    for command, func in commands:
        check_command(command, func)


def test_filesystem():
    iterate_commands(FILESYSTEM_COMMANDS)


def test_network():
    iterate_commands(NETWORK_COMMANDS)
