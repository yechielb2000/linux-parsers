from linux_parsers.parsers.filesystem.mount import parse_mount


def test_mount():
    command_output = """
/dev/sda1 / ext4 rw,relatime,data=ordered 0 0
/dev/sdb1 /mnt ext4 rw,relatime,data=ordered 0 0
/dev/sdc1 /home ext4 rw,relatime,data=ordered 0 0
/dev/sr0 /media/cdrom iso9660 ro,nosuid,nodev,relatime 0 0
tmpfs /tmp tmpfs rw,nosuid,nodev 0 0
proc /proc proc rw,nosuid,nodev,noexec,relatime 0 0
sysfs /sys sysfs rw,nosuid,nodev,noexec,relatime 0 0
/dev/mapper/vg1-lv1 /mnt/data ext4 rw,relatime,data=ordered 0 0
/dev/sdd1 /mnt/usb vfat rw,nosuid,nodev,relatime,uid=1000,gid=1000 0 0
nfs-server:/exported/path /mnt/nfs nfs4 rw,relatime,vers=4.2,rsize=1048576,wsize=1048576,timeo=600,retrans=2 0 0
"""
    parsed_command = parse_mount(command_output)
    assert len(parsed_command) == 10
    assert parsed_command[0]["device"] == "/dev/sda1"
    assert parsed_command[0]["dump"] == "0"
    assert parsed_command[4]["device"] == "tmpfs"
    assert parsed_command[8]["filesystem_type"] == "vfat"
