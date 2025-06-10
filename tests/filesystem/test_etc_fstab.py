from linux_parsers.parsers.filesystem.etc_fstab import parse_etc_fstab


def test_etc_fstab():
    command_output = """
# /etc/fstab: static file system information.
#
# <file system>   <mount point>   <type>   <options>         <dump> <pass>

UUID=6e4f2f3a-4d2f-4d7a-9e00-6f2e5c3a7bde   /            ext4    defaults          0       1
UUID=8923a8f2-3e8e-4e9f-8050-2e40f1e8d9cd   /home        ext4    defaults          0       2
UUID=ae28f6f1-b3f2-43e1-a938-18b292c12a23   swap         swap    sw                0       0
/dev/sdb1                                 /mnt/backup   ext4    noauto,nofail     0       2
//192.168.1.100/share                     /mnt/share    cifs    credentials=/root/.smbcred,uid=1000,gid=1000  0  0    
"""
    parsed_output = parse_etc_fstab(command_output)
    assert parsed_output[0] == {
        "device": "UUID=6e4f2f3a-4d2f-4d7a-9e00-6f2e5c3a7bde",
        "dump": "0",
        "filesystem_type": "ext4",
        "mount_point": "/",
        "options": "defaults",
        "pass": "1",
    }
    assert parsed_output[1] == {
        "device": "UUID=8923a8f2-3e8e-4e9f-8050-2e40f1e8d9cd",
        "dump": "0",
        "filesystem_type": "ext4",
        "mount_point": "/home",
        "options": "defaults",
        "pass": "2",
    }
