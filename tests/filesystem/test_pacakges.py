from linux_parsers.parsers.filesystem import (
    parse_dpkg_l,
    parse_flatpak_list,
    parse_rpm_qa,
    parse_snap_list,
    parse_yum_list_installed,
)


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


def test_dpkg_l():
    command_output = """
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version                                       Architecture Description
+++-===============================-=============================================-============-================================================================================
ii  ack                             3.7.0-1                                       all          grep-like program specifically for large source trees
ii  adduser                         3.137                                         all          add and remove users and groups
ii  apparmor                        3.1.7-1+b3                                    amd64        event-space parser utility for AppArmor
ii  apt                             2.9.5+kali1                                   amd64        commandline package manager    
"""
    parsed_output = parse_dpkg_l(command_output)
    assert len(parsed_output) == 4
    assert parsed_output[0] == {
        "arch": "all",
        "description": "grep-like program specifically for large source trees",
        "name": "ack",
        "version": "3.7.0-1",
    }
    assert parsed_output[1] == {
        "arch": "all",
        "description": "add and remove users and groups",
        "name": "adduser",
        "version": "3.137",
    }


def test_parse_yum_list_installed():
    """Test parsing of 'yum list installed' command output."""
    command_output = """
Loaded plugins: fastestmirror, langpacks
Installed Packages
acl.x86_64                           2.2.51-15.el7                   @anaconda
audit.x86_64                         2.8.5-4.el7                     @base
audit-libs.x86_64                    2.8.5-4.el7                     @anaconda
basesystem.noarch                    10.0-7.el7.centos                @anaconda
bash.x86_64                          4.2.46-34.el7                   @base
bind-libs-lite.x86_64               9.11.4-26.P2.el7_9.13           @updates
bind-license.noarch                  9.11.4-26.P2.el7_9.13           @updates
binutils.x86_64                      2.27-44.base.el7_9.1            @updates
ca-certificates.noarch               2021.2.50-72.el7_9              @updates
centos-release.x86_64                7-9.2009.1.el7.centos           @anaconda
"""

    parsed_packages = parse_yum_list_installed(command_output)

    # Check that we parsed the expected number of packages
    assert len(parsed_packages) == 10

    # Check specific package details
    acl_package = parsed_packages[0]
    assert acl_package["name"] == "acl"
    assert acl_package["version"] == "2.2.51"
    assert acl_package["release"] == "15.el7"
    assert acl_package["architecture"] == "x86_64"
    assert acl_package["repository"] == "@anaconda"

    # Check another package
    bash_package = parsed_packages[4]
    assert bash_package["name"] == "bash"
    assert bash_package["version"] == "4.2.46"
    assert bash_package["release"] == "34.el7"
    assert bash_package["architecture"] == "x86_64"
    assert bash_package["repository"] == "@base"

    # Check noarch package
    basesystem_package = parsed_packages[3]
    assert basesystem_package["name"] == "basesystem"
    assert basesystem_package["version"] == "10.0"
    assert basesystem_package["release"] == "7.el7.centos"
    assert basesystem_package["architecture"] == "noarch"
    assert basesystem_package["repository"] == "@anaconda"


def test_parse_yum_list_installed_empty():
    """Test parsing of empty yum output."""
    command_output = """
Loaded plugins: fastestmirror, langpacks
Installed Packages
"""

    parsed_packages = parse_yum_list_installed(command_output)
    assert len(parsed_packages) == 0


def test_parse_yum_list_installed_minimal():
    """Test parsing of minimal yum output with one package."""
    command_output = """
Installed Packages
kernel.x86_64                        3.10.0-1160.el7                 @anaconda
"""

    parsed_packages = parse_yum_list_installed(command_output)
    assert len(parsed_packages) == 1

    package = parsed_packages[0]
    assert package["name"] == "kernel"
    assert package["version"] == "3.10.0"
    assert package["release"] == "1160.el7"
    assert package["architecture"] == "x86_64"
    assert package["repository"] == "@anaconda"


def test_parse_snap_list():
    command_output = """Name               Version                     Rev    Tracking       Publisher   Notes
core18             20211028                    2128   latest/stable  canonical✓  base
core20             20220527                    1518   latest/stable  canonical✓  base
firefox            105.0.1-1                   1969   latest/stable  mozilla✓    -
gnome-3-38-2004    0+git.efb213a               119    latest/stable  canonical✓  -
gtk-common-themes  0.1-81-g442e511             1535   latest/stable  canonical✓  -
snap-store         41.3-64-gde65ba7            558    latest/stable  canonical✓  -
snapd              2.57.5                      17336  latest/stable  canonical✓  snapd
code               1.72.2-1665614327           108    latest/stable  vscode✓     classic
discord            0.0.20                      140    latest/stable  discord✓    -
"""

    parsed_command = parse_snap_list(command_output)

    assert len(parsed_command) == 9

    # Test first package
    assert parsed_command[0]["name"] == "core18"
    assert parsed_command[0]["version"] == "20211028"
    assert parsed_command[0]["rev"] == "2128"
    assert parsed_command[0]["tracking"] == "latest/stable"
    assert parsed_command[0]["publisher"] == "canonical✓"
    assert parsed_command[0]["notes"] == "base"

    # Test package with classic notes
    code_snap = next(pkg for pkg in parsed_command if pkg["name"] == "code")
    assert code_snap["version"] == "1.72.2-1665614327"
    assert code_snap["notes"] == "classic"

    # Test package with no notes (-)
    firefox_snap = next(pkg for pkg in parsed_command if pkg["name"] == "firefox")
    assert firefox_snap["version"] == "105.0.1-1"
    assert firefox_snap["notes"] == "-"

    # Test snapd package
    snapd_snap = next(pkg for pkg in parsed_command if pkg["name"] == "snapd")
    assert snapd_snap["notes"] == "snapd"


def test_flatpak_list():
    command_output = """Name                           Application ID                            Version       Branch   Installation
Bottles                        com.usebottles.bottles                    51.14         stable   system
Calculator                     org.gnome.Calculator                      46.0          stable   system
Cheese                         org.gnome.Cheese                          44.1          stable   system
Document Viewer               org.gnome.Evince                          46.3.1        stable   system
Extension Manager             com.mattjakeman.ExtensionManager          0.5.1         stable   system
Files                         org.gnome.Nautilus                       46.2          stable   system
Firefox                       org.mozilla.firefox                       131.0.3       stable   system
GNOME Text Editor             org.gnome.TextEditor                      46.3          stable   system
Image Viewer                  org.gnome.eog                            46.0          stable   system
LibreOffice                   org.libreoffice.LibreOffice               24.8.2.1      stable   system
Videos                        org.gnome.Totem                          43.0          stable   system
VS Code                       com.visualstudio.code                     1.95.2        stable   user
"""
    parsed_command = parse_flatpak_list(command_output)
    assert len(parsed_command) == 12
    assert parsed_command[0]["name"] == "Bottles"
    assert parsed_command[0]["application_id"] == "com.usebottles.bottles"
    assert parsed_command[0]["version"] == "51.14"
    assert parsed_command[0]["branch"] == "stable"
    assert parsed_command[0]["installation"] == "system"
    assert parsed_command[11]["name"] == "VS Code"
    assert parsed_command[11]["application_id"] == "com.visualstudio.code"
    assert parsed_command[11]["installation"] == "user"
