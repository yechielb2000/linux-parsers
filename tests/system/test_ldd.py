from linux_parsers.parsers.system.ldd import parse_ldd


def test_ldd():
    command_output = """
linux-vdso.so.1 (0x00007ffc8d1dc000)
        libjemalloc.so.2 => /lib/x86_64-linux-gnu/libjemalloc.so.2 (0x00007f52f9c89000)
        libisc-9.20.0-Debian.so => /lib/x86_64-linux-gnu/libisc-9.20.0-Debian.so (0x00007f52f9bf8000)
        libdns-9.20.0-Debian.so => /lib/x86_64-linux-gnu/libdns-9.20.0-Debian.so (0x00007f52f99bc000)
        libisccfg-9.20.0-Debian.so => /lib/x86_64-linux-gnu/libisccfg-9.20.0-Debian.so (0x00007f52f996e000)    
"""
    parsed_output = parse_ldd(command_output)
    assert len(parsed_output) == 5
    assert parsed_output[0] == {"address": "0x00007ffc8d1dc000", "path": None, "program": "linux-vdso.so.1"}
    assert parsed_output[4] == {
        "address": "0x00007f52f996e000",
        "path": "/lib/x86_64-linux-gnu/libisccfg-9.20.0-Debian.so",
        "program": "libisccfg-9.20.0-Debian.so",
    }
