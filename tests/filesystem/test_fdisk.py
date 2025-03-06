from linux_parsers.parsers.filesystem.fdisk import parse_fdisk


def test_fdisk():
    command_output = """
Disk /dev/sda: 500 GiB, 536870912000 bytes, 1048576000 sectors
Disk model: Samsung SSD 860  
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: C1D2E3F4-G5H6-I7J8-K9L0-M1N2O3P4Q5R6

Device         Start        End    Sectors   Size Type
/dev/sda1       2048    1050623    1048576   512M EFI System
/dev/sda2    1050624   84049919   82999296  39.6G Linux filesystem
/dev/sda3   84049920  104857599   20807680   9.9G Linux swap
/dev/sda4  104857600  209715199  104857600    50G Windows recovery environment
/dev/sda5  209715200  419430399  209715200   100G Microsoft basic data
/dev/sda6  419430400  524287999  104857600    50G **Filesystem errors detected**
/dev/sda7  524288000  629145599  104857600    50G **Unallocated space detected**

Disk /dev/sdb: 2 TiB, 2199023255552 bytes, 4294967296 sectors
Disk model: WD Black 2TB  
Units: sectors of 1 * 4096 = 4096 bytes
Sector size (logical/physical): 4096 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disklabel type: dos
Disk identifier: 1234ABCD

Device     Boot   Start        End    Sectors   Size Id Type
/dev/sdb1  *      2048   4294967295  4294965248   2T  7 HPFS/NTFS/exFAT

**Warning: Partition table entries are not in disk order.**
**Error: Partition /dev/sdb1 overlaps with another partition.**
**Warning: GPT detected on ‘/dev/sdb’ but it is being used with a MBR disklabel.**
    """
    parsed_command = parse_fdisk(command_output)
    assert parsed_command