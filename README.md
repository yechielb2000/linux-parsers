# Linux Parsers

## 🤵‍♂️ 🐧 🤵‍♀️ 🐧 🤵 🐧

    ^________________________________________________________
    |                                                        |
    | Simplest library for parsing linux commands and files  |
    \________________________________________________________/

## How to use

Let's say you want to parse `ps aux` command to get the processes in a better form.

```python
import subprocess
from linux_parsers.parsers.process.ps import parse_ps_aux

# Run the ps aux command
completed_process_result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# Get the command result
ps_aux_command_output = completed_process_result.stdout
# parse the command
parsed_command_output = parse_ps_aux(ps_aux_command_output)
# Print the parsed command result
print(parsed_command_output)
```

## Hierarchy

#### Filesystem parsers

- [df.py](linux_parsers/parsers/filesystem/df.py) - parse commands: `df`.
- [dpkg.py](linux_parsers/parsers/filesystem/dpkg.py) - parse commands: `dpkg -l`.
- [du.py](linux_parsers/parsers/filesystem/du.py) - parse commands: `du -ab <path>`.
- [fdisk.py](linux_parsers/parsers/filesystem/fdisk.py) - parse commands: `fdisk -l`.
- [ls.py](linux_parsers/parsers/filesystem/ls.py) - parse commands: `ls -la`.
- [mount.py](linux_parsers/parsers/filesystem/mount.py) - parse file `/proc/mounts` or command `mount`.
- [stat.py](linux_parsers/parsers/filesystem/stat.py) - parse commands: `stat`.

#### Network parsers

- [arp.py](linux_parsers/parsers/network/arp.py) - parse commands: `arp -i <interface>`, `arp -en`, `arp -e`.
- [etc_resolve_conf.py](linux_parsers/parsers/network/etc_resolve_conf.py) - parse file: `/etc/resolve.conf`.
- [ip.py](linux_parsers/parsers/network/ip.py) - parse commands: `ip a`, `ip r`, `ip n`.
- [iptables.py](linux_parsers/parsers/network/iptables.py) - parse commands: `iptables -L -n -v`.
- [netstat.py](linux_parsers/parsers/network/netstat.py) - parse commands: `netstat -tulpan`.
- [ping.py](linux_parsers/parsers/network/ping.py) - parse commands: `ping <address>`.
- [ss.py](linux_parsers/parsers/network/ss.py) - parse commands: `ss -tulnap`, `ss -s`.
- [ufw.py](linux_parsers/parsers/network/ufw.py) - parse commands: `ufw app list`, `ufw status`.

#### Process parsers

- [cgroups.py](linux_parsers/parsers/process/cgroups.py) - parse files: `/proc/cgroups`, `/proc/<pid>/cgroups`.
- [jobs.py](linux_parsers/parsers/process/jobs.py) - parse commands: `jobs`.
- [ps.py](linux_parsers/parsers/process/ps.py) - parse commands: `ps aux`, `ps -ax`,`ps -caweL`, `ps -fadel`.
- [top.py](linux_parsers/parsers/process/top.py) - parse commands: `top`.
- [lsipc.py](linux_parsers/parsers/process/lsipc.py) - parse commands: `lsipc`.

#### Session parsers

- [last.py](linux_parsers/parsers/session/last.py) - parse commands: `last`.
- [w.py](linux_parsers/parsers/session/w.py) - parse commands: `w`.
- [who.py](linux_parsers/parsers/session/who.py) - parse commands: `who -a`.
- [ac.py](linux_parsers/parsers/session/ac.py) - parse commands: `ac -d`, `ac -p`, `ac -pd`.

#### System parsers

- [etc_os_release.py](linux_parsers/parsers/system/etc_os_release.py) - parse file: `/etc/os-release`.
- [free.py](linux_parsers/parsers/system/free.py) - parse commands: `free -btlv`.
- [hwinfo.py](linux_parsers/parsers/system/hwinfo.py) - parse commands: `hwinfo --<action>`.
- [iostat.py](linux_parsers/parsers/system/iostat.py) - parse commands: `iostat -x`.
- [mpstat.py](linux_parsers/parsers/system/mpstat.py) - parse commands: `mpstat -P ALL`.
- [proc_cpuinfo.py](linux_parsers/parsers/system/proc_cpuinfo.py) - parse file: `/proc/cpuinfo`.
- [proc_meminfo.py](linux_parsers/parsers/system/proc_meminfo.py) - parse file: `/proc/meminfo`.
- [proc_devices.py](linux_parsers/parsers/system/proc_devices.py) - parse file: `/proc/devices`
- [proc_uptime.py](linux_parsers/parsers/system/proc_uptime.py) - parse file: `/proc/uptime`
- [service.py](linux_parsers/parsers/system/service.py) - parse commands: `service --status-all`.
- [etc_systemd_file_conf.py](linux_parsers/parsers/system/etc_systemd_file_conf.py) - parse files:
  `/etc/systemd/*.conf`.
- [uname.py](linux_parsers/parsers/system/uname.py) - parse commands: `uname -a`.
- [vmstat.py](linux_parsers/parsers/system/vmstat.py) - parse commands: `vmstat`, `vmstat -adt`.

#### Users parsers

- [chage.py](linux_parsers/parsers/users/chage.py) - parse commands: `chage -l <username>`.
- [etc_group.py](linux_parsers/parsers/users/etc_group.py) - parse file: `/etc/group`.
- [etc_gshadow.py](linux_parsers/parsers/users/etc_gshadow.py) - parse file: `/etc/gshadow`.
- [etc_passwd.py](linux_parsers/parsers/users/etc_passwd.py) - parse file: `/etc/passwd`.
- [etc_shadow.py](linux_parsers/parsers/users/etc_shadow.py) - parse file: `/etc/shadow`.
- [useradd.py](linux_parsers/parsers/users/useradd.py) - parse commands: `useradd -D`.

## Contribute

Thank you for considering contributing to this project! Whether you want to add parsers, fix bugs, or enhance the
project, your contributions are welcome. Follow the instructions below to get started.

### How to Contribute

1. **Fork the Repository**  
   Click the "Fork" button on the top-right of this repository to create your own copy.

2. **Clone Your Fork**  
   Clone the repository to your local machine:
   ```shell
   git clone https://github.com/yechielb2000/linux-parsers.git
   ```

3. **Set Up the Project**  
   Navigate into the project directory:
   ```shell
   cd linux-parsers
   ```

   Install dependencies and set up pre-commit hooks:
   ```shell
   uv sync
   uv run pre-commit run --all-files
   ```

   This will ensure everything is up to date and that the code is formatted according to the project's standards.

4. **Create a New Branch**  
   Always create a new branch for your changes. The branch name should follow this convention:
    - **Bug fixes**: `bugfix/parsername`
    - **New parsers**: `feature/parsername`
    - **Refactors**: `refactor/parsername`

   Example:
   ```shell
   git checkout -b feature/new-parser
   ```

5. **Make Your Changes**  
   Add your parser or make any changes to the code. Ensure your changes are thoroughly tested and adhere to the
   project's guidelines.

6. **Commit Your Changes**  
   After making your changes, commit them with a clear message:
   ```shell
   git commit -m "Add new parser for XYZ"
   ```

7. **Push Your Changes**  
   Push your changes to your fork:
   ```shell
   git push origin feature/new-parser
   ```

8. **Create a Pull Request**  
   Go to the original repository on GitHub and create a pull request (PR) from your fork. Make sure to target the `main`
   branch. Provide a clear description of the changes in your PR, referencing any relevant issues.

---

### Thank You!

We greatly appreciate your contributions to this project! Your work helps improve the project for everyone. If you have
any questions or need help, don't hesitate to reach out.
