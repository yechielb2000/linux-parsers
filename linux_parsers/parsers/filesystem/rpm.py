from typing import Dict, List


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
