### 0.2.4 12.04.2025

- Added command parser: `ldd --version`, `ldd -v <program>`, `ldd <program>`.

### 0.2.3 05.04.2025

- Added command parser: `ac`.
- Added command parser: `lsipc`.
- Added file parser: `/proc/devices`

### 0.2.2 18.03.2025

- Added file parser: `/proc/uptime`.
- Added file parser: `/etc/systemd/*.conf`.

#### For Developers

- Added pre-commit hooks.
- Added linter and tests workflows.
- Added tests for windows and linux in python versions from `3.9` to `3.13`.
- Updated pyproject configurations for pytest and ruff.
- Updated readme in the contributions section.

### 0.2.1 18.03.2025

- Bugfix: fix type annotations for python `3.8`.

### 0.2.0 17.03.2025

- Update python support to `>=3.8`.