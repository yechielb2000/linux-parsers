from linux_parsers.parsers.filesystem.df import parse_df


def test_df():
    command_output = """
Filesystem      1K-blocks      Used Available Use% Mounted on
none              4037644         0   4037644   0% /usr/lib/modules/5.15.167.4-microsoft-standard-WSL2
none              4037644         4   4037640   1% /mnt/wsl
drivers         248904004 214140520  34763484  87% /usr/lib/wsl/drivers
/dev/sdc       1055762868   8968000 993091396   1% /
none              4037644       120   4037524   1% /mnt/wslg
none              4037644         0   4037644   0% /usr/lib/wsl/lib
rootfs            4034232      2208   4032024   1% /init
none              4034232         0   4034232   0% /dev
none              4037644         4   4037640   1% /run
none              4037644         0   4037644   0% /run/lock
none              4037644         0   4037644   0% /run/shm
none              4037644         0   4037644   0% /run/user
tmpfs             4037644         0   4037644   0% /sys/fs/cgroup
none              4037644        76   4037568   1% /mnt/wslg/versions.txt
none              4037644        76   4037568   1% /mnt/wslg/doc
C:\             248904004 214140520  34763484  87% /mnt/c
    """
    parsed_command = parse_df(command_output)
    assert parsed_command[5]["Filesystem"] == "none"
    assert parsed_command[1]["Blocks"] == "4037644"
    assert parsed_command[2]["UsePercent"] == "87"
