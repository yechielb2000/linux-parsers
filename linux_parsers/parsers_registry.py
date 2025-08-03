from collections import ChainMap

from linux_parsers.parsers.filesystem import stat, df, du, ls, mount, fdisk, dpkg
from linux_parsers.parsers.network import ss, arp, ip, ping, ufw, netstat, iptables
from linux_parsers.parsers.process import ps, top, jobs, lsipc, cgroups
from linux_parsers.parsers.session import w, ac, who, last
from linux_parsers.parsers.system import ldd, free, lsmod, uname, hwinfo, iostat, mpstat, vmstat, service
from linux_parsers.parsers.users import chage, useradd

NETWORK_REGISTRY = {
    "ss": [
        {
            "must_have": {"-s"},
            "one_of": set(),
            "parser": ss.parse_ss_s,
        },
        {
            "must_have": {"-t", "-u", "-l", "-n", "-a", "-p"},
            "one_of": set(),
            "parser": ss.parse_ss_tulnap,
        },
    ],
    "arp": [
        {
            "must_have": set(),
            "one_of": {"-i", "-e", "-n"},
            "parser": arp.parse_arp,
        }
    ],
    "ip": [
        {
            "subcommand_aliases": ["a", "addr", "address"],
            "must_have": set(),
            "one_of": set(),
            "parser": ip.parse_ip_a,
        },
        {
            "subcommand_aliases": ["n"],
            "must_have": set(),
            "one_of": set(),
            "parser": ip.parse_ip_n,
        },
        {
            "subcommand_aliases": ["r", "route"],
            "must_have": set(),
            "one_of": set(),
            "parser": ip.parse_ip_r,
        },
    ],
    "ping": [
        {
            "must_have": set(),
            "one_of": set(),
            "parser": ping.parse_ping,
        }
    ],
    "ufw": [
        {
            "subcommand_aliases": ["status"],
            "must_have": set(),
            "one_of": set(),
            "parser": ufw.parse_ufw_status,
        },
        {
            "subcommand_aliases": ["app"],  # assuming "list" comes right after.
            "must_have": set(),
            "one_of": set(),
            "parser": ufw.parse_ufw_app_list,
        },
    ],
    "netstat": [
        {
            "must_have": {"-t", "-u", "-l", "-p", "-a", "-n"},
            "one_of": set(),
            "parser": netstat.parse_netstat,
        }
    ],
    "iptables": [
        {
            "must_have": {"-L", "-n", "-v"},
            "one_of": set(),
            "parser": iptables.parse_iptables,
        }
    ],
}

SYSTEM_REGISTRY = {
    "ldd": [
        {
            "must_have": set(),
            "one_of": set(),
            "parser": ldd.parse_ldd,
        },
        {
            "must_have": {"-v"},
            "one_of": set(),
            "parser": ldd.parse_ldd_verbose,
        },
        {
            "must_have": {"--version"},
            "one_of": set(),
            "parser": ldd.parse_ldd_version,
        },
    ],
    "free": [
        {
            "must_have": {"-b", "-t", "-l", "-v"},
            "one_of": set(),
            "parser": free.parse_free_btlv,
        }
    ],
    "lsmod": [
        {
            "must_have": set(),
            "one_of": set(),
            "parser": lsmod.parse_lsmod,
        }
    ],
    "uname": [
        {
            "must_have": {"-a"},
            "one_of": set(),
            "parser": uname.parse_uname_a,
        }
    ],
    "hwinfo": [
        {
            "must_have": set(),
            "one_of": {"--cpu", "--memory", "--disk", "--network", "--usb", "--gfxcard", "--bluetooth"},
            "parser": hwinfo.parse_hwinfo,
        }
    ],
    "iostat": [
        {
            "must_have": {"-x"},
            "one_of": set(),
            "parser": iostat.parse_iostat,
        }
    ],
    "mpstat": [
        {
            "must_have": {"-P"},
            "one_of": set(),
            "parser": mpstat.parse_mpstat,
        }
    ],
    "vmstat": [
        {
            "must_have": set(),
            "one_of": set(),
            "parser": vmstat.parse_vmstat,
        },
        {
            "must_have": {"-a", "-d", "-t"},
            "one_of": set(),
            "parser": vmstat.parse_vmstat_adt,
        },
    ],
    "service": [
        {
            "must_have": {"--status-all"},
            "one_of": set(),
            "parser": service.parse_service,
        }
    ],
}

SESSION_REGISTRY = {
    "w": [
        {
            "must_have": set(),
            "one_of": set(),
            "parser": w.parse_w,
        }
    ],
    "ac": [
        {
            "must_have": {"-d", "-p"},
            "one_of": set(),
            "parser": ac.parse_ac_pd,
        },
        {
            "must_have": {"-d"},
            "one_of": set(),
            "parser": ac.parse_ac_d,
        },
        {
            "must_have": {"-p"},
            "one_of": set(),
            "parser": ac.parse_ac_p,
        },
    ],
    "who": [
        {
            "must_have": {"-a"},
            "one_of": set(),
            "parser": who.parse_who_a,
        }
    ],
    "last": [
        {
            "must_have": set(),
            "one_of": set(),
            "parser": last.parse_last,
        }
    ],
}

FILESYSTEM_REGISTRY = {
    "stat": [
        {
            "must_have": set(),
            "one_of": set(),
            "parser": stat.parse_stat,
        }
    ],
    "df": [
        {
            "must_have": set(),
            "one_of": set(),
            "parser": df.parse_df,
        }
    ],
    "du": [
        {
            "must_have": {"-a", "-b"},
            "one_of": set(),
            "parser": du.parse_du,
        }
    ],
    "ls": [
        {
            "must_have": {"-l", "-a"},
            "one_of": set(),
            "parser": ls.parse_ls,
        }
    ],
    "mount": [
        {
            "must_have": set(),
            "one_of": set(),
            "parser": mount.parse_mount,
        }
    ],
    "fdisk": [
        {
            "must_have": {"-l"},
            "one_of": set(),
            "parser": fdisk.parse_fdisk,
        }
    ],
    "dpkg": [
        {
            "must_have": {"-l"},
            "one_of": set(),
            "parser": dpkg.parse_dpkg_l,
        }
    ],
}

PROCESS_REGISTRY = {
    "ps": [
        {
            "must_have": set(),
            "subcommand_aliases": ["aux"],
            "one_of": set(),
            "parser": ps.parse_ps_aux,
        },
        {
            "must_have": {"-a", "-x"},
            "one_of": set(),
            "parser": ps.parse_ps_ax,
        },
        {
            "must_have": {"c", "a", "w", "e", "L"},
            "one_of": set(),
            "parser": ps.parse_ps_caweL,
        },
        {
            "must_have": {"f", "a", "d", "e", "l"},
            "one_of": set(),
            "parser": ps.parse_ps_fadel,
        },
    ],
    "top": [
        {
            "must_have": set(),
            "one_of": set(),
            "parser": top.parse_top,
        }
    ],
    "jobs": [
        {
            "must_have": set(),
            "one_of": set(),
            "parser": jobs.parse_jobs,
        }
    ],
    "lsipc": [
        {
            "must_have": set(),
            "one_of": set(),
            "parser": lsipc.parse_lsipc,
        }
    ],
    "systemd-cgls": [
        {
            "must_have": set(),
            "one_of": {"-a", "-l"},
            "parser": cgroups.parse_cgroup_pid_list,
        }
    ],
}

USERS_REGISTRY = {
    "chage": [
        {
            "must_have": {"-l"},
            "one_of": set(),
            "parser": chage.parse_chage_l,
        }
    ],
    "useradd": [
        {
            "must_have": {"-D"},
            "one_of": set(),
            "parser": useradd.parse_useradd_D,
        }
    ],
}

PARSER_REGISTRY = ChainMap(NETWORK_REGISTRY, SYSTEM_REGISTRY, SESSION_REGISTRY, FILESYSTEM_REGISTRY, PROCESS_REGISTRY)
