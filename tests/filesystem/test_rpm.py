"""Tests for rpm command parser."""

from linux_parsers.parsers.filesystem.rpm import parse_rpm_qa


def test_rpm_qa():
    """Test parsing of rpm -qa command output."""
    command_output = """
glibc-2.17-326.el7_9.x86_64
kernel-3.10.0-1160.76.1.el7.x86_64
openssh-7.4p1-22.el7_9.x86_64
python3-3.6.8-18.el7.x86_64
systemd-219-78.el7_9.7.x86_64
bash-4.2.46-35.el7_9.x86_64
curl-7.29.0-59.el7_9.1.x86_64
vim-enhanced-7.4.629-8.el7_9.x86_64
httpd-2.4.6-97.el7_9.x86_64
mysql-community-server-8.0.32-1.el7.x86_64
"""

    parsed_packages = parse_rpm_qa(command_output)

    assert len(parsed_packages) == 10

    # Test first package
    assert parsed_packages[0]["name"] == "glibc"
    assert parsed_packages[0]["version"] == "2.17"
    assert parsed_packages[0]["release"] == "326.el7_9"
    assert parsed_packages[0]["architecture"] == "x86_64"
    assert parsed_packages[0]["full_name"] == "glibc-2.17-326.el7_9.x86_64"

    # Test package with hyphens in the name
    assert parsed_packages[2]["name"] == "openssh"
    assert parsed_packages[2]["version"] == "7.4p1"
    assert parsed_packages[2]["release"] == "22.el7_9"

    # Test package with multiple hyphens in the name
    assert parsed_packages[3]["name"] == "python3"
    assert parsed_packages[3]["version"] == "3.6.8"
    assert parsed_packages[3]["release"] == "18.el7"

    # Test package with a complex name
    assert parsed_packages[7]["name"] == "vim-enhanced"
    assert parsed_packages[7]["version"] == "7.4.629"
    assert parsed_packages[7]["release"] == "8.el7_9"

    # Test package with a longer complex name
    assert parsed_packages[9]["name"] == "mysql-community-server"
    assert parsed_packages[9]["version"] == "8.0.32"
    assert parsed_packages[9]["release"] == "1.el7"
