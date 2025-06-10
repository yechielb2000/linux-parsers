### 0.2.5 10.06.2025

- Added file parser: `/etc/fstab`.
- Added logfile parser: `/var/log/secure`.
- Added logfile parser: `/var/log/dpkg.log`.
- Added logfile parser: `/var/log/auth.log`.
- Added logfile parser: `/var/log/cron`.
- Added logfile parser: `/var/log/syslog`.
- Added logfile parser: `/var/log/wtmp`
- Added logfile parser: `/var/log/utmp`
- Added logfile parser: `/var/log/btmp`

### 0.2.4 30.04.2025

- Added command parser: `ldd --version`, `ldd -v <program>`, `ldd <program>`.
- Added file parser: `/proc/version`.
- Added command parser: `systemd-cgls -al`.
- Added file parser: `/sys/fs/cgroup/<controller>/<cgroup_path>/cgroup.procs`.
- Added file parser: `/proc/modules`.

### 0.2.3 05.04.2025

- Added command parser: `ac`.
- Added command parser: `lsipc`.
- Added file parser: `/proc/devices`

### 0.2.2 18.03.2025

- Added file parser: `/proc/uptime`.
- Added file parser: `/etc/systemd/*.conf`.

### 0.2.1 18.03.2025

- Bugfix: fix type annotations for python `3.8`.

### 0.2.0 17.03.2025

- Update python support to `>=3.8`.