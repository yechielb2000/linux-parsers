import re

from typing import List, Dict, Any


def parse_dpkg_l(command_output: str) -> List[Dict[str, Any]]:
    """Parse `dpkg -l` command output."""
    pattern = re.compile(
        r"ii\s+(?P<name>\S+)\s+(?P<version>\S+)\s+(?P<arch>\S+)\s+(?P<description>.+)",
        flags=re.MULTILINE,
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]


def parse_rpm_qa(command_output: str) -> List[Dict[str, str]]:
    """Parse `rpm -qa` command output.

    The rpm -qa command lists all installed RPM packages.
    Each line contains a package name, version, release, and architecture.

    Args:
        command_output: Output from `rpm -qa` command

    Returns:
        List of dictionaries containing package information
    """
    parsed_packages = []

    for line in command_output.splitlines():
        if not line.strip():
            continue

        parts = line.rsplit(".", 1)
        package_part = parts[0]
        arch = parts[1] if len(parts) == 2 else None

        # Split by hyphens to separate name, version, and release
        hyphen_parts = package_part.split("-")

        pkg = {
            "name": "-".join(hyphen_parts[:-2]) if len(hyphen_parts) > 2 else hyphen_parts[0],
            "version": hyphen_parts[-2] if len(hyphen_parts) > 1 else None,
            "release": hyphen_parts[-1] if len(hyphen_parts) > 2 else None,
            "architecture": arch,
            "full_name": line.strip(),
        }

        parsed_packages.append(pkg)

    return parsed_packages


def parse_yum_list_installed(command_output: str) -> List[Dict]:
    """Parse `yum list installed` command output.

    Parses the output of 'yum list installed' which shows all installed packages
    on Red Hat-based systems (RHEL, CentOS, Fedora, etc.).

    The command shows packages in the format:
    package-name.architecture    version-release    repository

    Args:
        command_output: Raw output from 'yum list installed' command

    Returns:
        List of dictionaries containing package information with keys:
        - name: Package name
        - architecture: Package architecture
        - version: Package version
        - release: Package release
        - repository: Repository the package came from
    """
    parsed_packages = []

    # Skip the header lines and filter empty lines
    lines = [line.strip() for line in command_output.splitlines() if line.strip()]

    # Skip header lines that typically start with "Installed Packages" or "Loaded plugins"
    data_lines = []
    for line in lines:
        if not (
            line.startswith("Loaded plugins")
            or line.startswith("Installed Packages")
            or line.startswith("Available Packages")
            or line == ""
        ):
            data_lines.append(line)

    for line in data_lines:
        # Match package lines with format: package.arch version repository
        # Some lines might be continuation lines starting with whitespace
        if line.startswith(" ") or line.startswith("\t"):
            continue

        # Split the line into parts
        parts = line.split()
        if len(parts) >= 3:
            # Parse package name and architecture
            package_full = parts[0]
            if "." in package_full:
                package_name, architecture = package_full.rsplit(".", 1)
            else:
                package_name = package_full
                architecture = ""

            # Parse version and release
            version_release = parts[1]
            if "-" in version_release:
                # Split version-release, but be careful as version might contain dashes
                version_parts = version_release.split("-")
                if len(version_parts) >= 2:
                    version = "-".join(version_parts[:-1])
                    release = version_parts[-1]
                else:
                    version = version_release
                    release = ""
            else:
                version = version_release
                release = ""

            # Repository is the third part
            repository = parts[2] if len(parts) > 2 else ""

            parsed_packages.append(
                {
                    "name": package_name,
                    "architecture": architecture,
                    "version": version,
                    "release": release,
                    "repository": repository,
                }
            )

    return parsed_packages


def parse_snap_list(command_output: str) -> List[Dict[str, str]]:
    """Parse `snap list` command output.

    Parses the output of 'snap list' which shows all installed snap packages
    on Ubuntu and other Linux distributions that support snap.

    The command shows packages in the format:
    Name    Version    Rev    Tracking       Publisher   Notes

    Args:
        command_output: Raw output from 'snap list' command

    Returns:
        List of dictionaries containing package information with keys:
        - name: Package name
        - version: Package version
        - rev: Revision number
        - tracking: Tracking channel
        - publisher: Publisher name
        - notes: Additional notes (like devmode, classic, etc.)
    """
    parsed_packages = []

    lines = [line for line in command_output.splitlines() if line.strip()]

    # Skip header line
    if lines and lines[0].startswith("Name"):
        lines = lines[1:]

    for line in lines:
        if not line.strip():
            continue

        # Split the line by whitespace
        parts = line.split()
        if len(parts) < 5:
            continue

        name = parts[0]
        version = parts[1]
        rev = parts[2]
        tracking = parts[3]
        publisher = parts[4]

        # Notes might be missing or contain spaces, so join remaining parts
        notes = " ".join(parts[5:]) if len(parts) > 5 else ""

        parsed_packages.append(
            {"name": name, "version": version, "rev": rev, "tracking": tracking, "publisher": publisher, "notes": notes}
        )

    return parsed_packages
