from linux_parsers.parsers.system.proc_devices import parse_proc_devices


def test_proc_devices():
    command_output = """
Character devices:
  1 mem
  4 /dev/vc/0
  4 tty
  5 /dev/console

Block devices:
  1 ramdisk
  7 loop
"""
    parsed_command = parse_proc_devices(command_output)
    character_devices = parsed_command.get("character_devices")
    block_devices = parsed_command.get("block_devices")
    assert character_devices is not None
    assert block_devices is not None
    assert len(character_devices) == 4
    assert len(block_devices) == 2
    assert character_devices[0]["major_num"] == "1"
    assert character_devices[0]["name"] == "mem"
    assert block_devices[0]["major_num"] == "1"
    assert block_devices[0]["name"] == "ramdisk"
