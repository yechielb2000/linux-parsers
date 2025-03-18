from linux_parsers.parsers.filesystem.stat import parse_stat


def test_stat():
    command_output = """
  File: filename
  Size: 12345       Blocks: 24         IO Block: 4096   regular file
Device: 802h/2050d  Inode: 654321      Links: 1
Access: 2025-03-07 12:34:56.789012345 +0000
Modify: 2025-03-06 10:20:30.123456789 +0000
Change: 2025-03-06 10:25:00.987654321 +0000
 Birth: -
    """
    parsed_output = parse_stat(command_output)
    assert parsed_output["birth"] == "-"
    assert parsed_output["type"] == "regular file"
    assert parsed_output["io_block"] == "4096"
    assert parsed_output["access"] == "2025-03-07 12:34:56.789012345 +0000"
