from linux_parsers.parsers.system.lsmod import parse_lsmod


def test_lsmod():
    command_output = """
Module                  Size  Used by
usb_storage            65536  1
btusb                  45056  0
bluetooth             581632  5 btusb
snd_hda_codec_hdmi     49152  1
"""
    parsed_output = parse_lsmod(command_output)
    assert parsed_output[0] == {"name": "usb_storage", "size": 65536, "used_by_count": 1, "used_by_modules": []}
