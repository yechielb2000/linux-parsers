from linux_parsers.parsers.logs.var_log_udev import parse_var_log_udev


def test_parse_var_log_udev():
    command_output = """
UDEV  [12345.678901] add      /devices/pci0000:00/0000:00:14.0/usb1/1-2 (usb)
ACTION=add
DEVPATH=/devices/pci0000:00/0000:00:14.0/usb1/1-2
SUBSYSTEM=usb
DEVNAME=/dev/bus/usb/001/002
DEVTYPE=usb_device
PRODUCT=1d6b/2/100
TYPE=9/0/1
BUSNUM=001
DEVNUM=002
SEQNUM=1234

UDEV  [12345.789012] remove   /devices/pci0000:00/0000:00:14.0/usb1/1-3 (usb)
ACTION=remove
DEVPATH=/devices/pci0000:00/0000:00:14.0/usb1/1-3
SUBSYSTEM=usb
DEVNAME=/dev/bus/usb/001/003
DEVTYPE=usb_device
SEQNUM=1235
"""
    parsed_output = parse_var_log_udev(command_output)
    assert parsed_output[0] == {
        "ACTION": "add",
        "BUSNUM": "001",
        "DEVNAME": "/dev/bus/usb/001/002",
        "DEVNUM": "002",
        "DEVPATH": "/devices/pci0000:00/0000:00:14.0/usb1/1-2",
        "DEVTYPE": "usb_device",
        "PRODUCT": "1d6b/2/100",
        "SEQNUM": "1234",
        "SUBSYSTEM": "usb",
        "TYPE": "9/0/1",
        "action": "add",
        "devpath": "/devices/pci0000:00/0000:00:14.0/usb1/1-2",
        "subsystem": "usb",
        "timestamp": "12345.678901",
    }
