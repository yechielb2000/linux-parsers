from linux_parsers.parsers.filesystem.ls import parse_ls


def test_ls():
    command_output = """
 drwx------ 15 a       a         4096 Feb 10 20:21 .
drwxr-xr-x  3 root    root      4096 Oct  7 04:29 ..
drwxr-xr-x  3 a       a         4096 Feb  9 16:38 2025-2-10
lrwxrwxrwx  1 a       a           23 Nov 28 15:04 .aws -> /mnt/c/Users/user/.aws
lrwxrwxrwx  1 a       a           25 Nov 28 15:04 .azure -> /mnt/c/Users/user/.azure
-rw-------  1 a       a       109924 Mar  6 17:06 .bash_history
-rw-r--r--  1 a       a          220 Oct  7 04:29 .bash_logout
-rw-r--r--  1 a       a         5551 Oct  7 04:29 .bashrc
-rw-r--r--  1 a       a         3526 Oct  7 04:29 .bashrc.original
drwxr-xr-x  3 root    root      4096 Dec 20 11:54 build
drwxr-xr-x  6 a       a         4096 Feb  7 14:45 .cache
-rwxrwxrwx  1 a       a       784611 Feb 10 20:20 code.zip
drwxr-xr-x  6 a       a         4096 Feb  7 14:45 .config
drwxr-xr-x  2 root    root      4096 Dec 20 11:57 dist
drwxr-xr-x  4 a       a         4096 Nov 28 15:04 .docker
-rw-r--r--  1 root    root       549 Nov 28 14:43 docker-compose.eck.kibana.redis.yml
drwxr-xr-x  4 a       a         4096 Feb  7 14:45 go
-rw-r--r--  1 tcpdump tcpdump     24 Jan 27 21:07 here.pcap
-rw-r--r--  1 a       a         3534 Dec 20 10:28 infoservice.py
-rw-r--r--  1 root    root       670 Dec 20 11:54 infoservice.spec
drwxr-xr-x  3 a       a         4096 Dec 20 12:02 .ipython
drwxr-xr-x  3 a       a         4096 Oct  7 04:29 .java
-rw-------  1 a       a           20 Oct  7 06:53 .lesshst
drwxr-xr-x  6 a       a         4096 Feb  7 14:44 .local
drwxr-xr-x  3 a       a         4096 Feb 10 20:21 __MACOSX
-rw-r--r--  1 a       a          807 Oct  7 04:29 .profile
drwx------  2 a       a         4096 Oct  7 06:48 .ssh
-rw-r--r--  1 a       a            0 Oct  7 06:53 .sudo_as_admin_successful
drwxr-xr-x  3 a       a         4096 Feb  9 00:06 webfuzz_api
-rw-r--r--  1 a       a          203 Feb  4 00:06 .wget-hsts
-rw-r--r--  1 a       a        10868 Oct  7 04:29 .zshrc   
    """
    parsed_command = parse_ls(command_output)
    assert parsed_command[1]['Permissions'] == 'drwxr-xr-x'
    assert parsed_command[2]['Group'] == 'a'
    assert parsed_command[1]['Size'] == '4096'
    assert parsed_command[14]['LastModified'] == 'Nov 28 15:04'