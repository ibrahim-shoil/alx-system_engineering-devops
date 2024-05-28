# 0x05 Processes and Signals

## Overview

This project focuses on processes and signals in the context of DevOps, Shell scripting, and Bash programming. The tasks involve writing Bash scripts to manage processes, understand signals, and create init scripts. Additionally, there's a C program to demonstrate the creation of zombie processes.

## Project Details

- **By**: Sylvain Kalache
- **Weight**: 1
- **Start Date**: Nov 24, 2023, 5:00 AM
- **End Date**: Nov 25, 2023, 5:00 AM
- **Checker Release**: Nov 24, 2023, 11:00 AM
- **Auto Review**: A review will be launched automatically at the deadline.

## Resources

Read or watch the following to gain a deeper understanding of the concepts covered in this project:

- [Linux PID](https://linux.die.net/man/5/proc)
- [Linux process](https://man7.org/linux/man-pages/man5/proc.5.html)
- [Linux signal](https://man7.org/linux/man-pages/man7/signal.7.html)
- [Process management in Linux](https://www.tldp.org/LDP/lpg/node5.html)

### Man pages

Refer to the following man pages for additional details:

- `ps`
- `pgrep`
- `pkill`
- `kill`
- `exit`
- `trap`

## Learning Objectives

By the end of this project, you are expected to be able to explain the following concepts without the help of Google:

1. What is a PID?
2. What is a process?
3. How to find a process’ PID.
4. How to kill a process.
5. What is a signal?
6. What are the 2 signals that cannot be ignored?

## Requirements

### General

- **Allowed Editors**: vi, vim, emacs
- **Interpreted On**: Ubuntu 20.04 LTS
- **File Endings**: All files should end with a new line
- **Shellcheck**: Your Bash script must pass Shellcheck (version 0.7.0 via apt-get) without any error
- **Bash Script Header**: The first line of all your Bash scripts should be `#!/usr/bin/env bash`
- **Script Comments**: The second line of all your Bash scripts should be a comment explaining what the script is doing

## Task Details

### 0. What is my PID

- Write a Bash script that displays its own PID.

```bash
sylvain@ubuntu$ ./0-what-is-my-pid
4120
sylvain@ubuntu$
```

### 1. List your processes

- Write a Bash script that displays a list of currently running processes.

```bash
sylvain@ubuntu$ ./1-list_your_processes | head -50
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         2  0.0  0.0      0     0 ?        S    Feb13   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ksoftirqd/0]
root         4  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/0:0]
...
sylvain@ubuntu$
```

### 2. Show your Bash PID

- Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

```bash
sylvain@ubuntu$ sylvain@ubuntu$ ./2-show_your_bash_pid
sylvain   4404  0.0  0.7  21432  4000 pts/0    Ss   03:32   0:00          \_ -bash
sylvain   4477  0.0  0.2  11120  1352 pts/0    S+   03:40   0:00              \_ bash ./2-show_your_bash_PID
sylvain   4479  0.0  0.1  10460   912 pts/0    S+   03:40   0:00                  \_ grep bash
sylvain@ubuntu$
```

### 3. Show your Bash PID made easy

- Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

```bash
sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4555 bash
sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4557 bash
sylvain@ubuntu$
```

### 4. To infinity and beyond

- Write a Bash script that displays To infinity and beyond indefinitely.

```bash
sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
^C
sylvain@ubuntu$
```

### 5. Don't stop me now!

- We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

- Write a Bash script that stops 4-to_infinity_and_beyond process.

Terminal #0

```bash
sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
sylvain@ubuntu$
```

Terminal #1

``` bash
sylvain@ubuntu$ ./5-dont_stop_me_now
sylvain@ubuntu$
```

### 6. Stop me if you can

- Write a Bash script that stops 4-to_infinity_and_beyond process.

Terminal #0

```bash
sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
sylvain@ubuntu$
```

Terminal #0

``` bash
sylvain@ubuntu$ ./6-stop_me_if_you_can
sylvain@ubuntu$ 
```

### 7. Highlander

-- Write a Bash script that displays:

- To infinity and beyond indefinitely
- With a sleep 2 in between each iteration
- I am invincible!!! when receiving a SIGTERM signal
- Make a copy of your 6-stop_me_if_you_can script, name it 67-stop_me_if_you_can, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

0. Terminal #0

```bash
sylvain@ubuntu$ ./7-highlander
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
I am invincible!!!
To infinity and beyond
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
^C
sylvain@ubuntu$
```

1. Terminal #1

```bash
sylvain@ubuntu$ ./67-stop_me_if_you_can
sylvain@ubuntu$ ./67-stop_me_if_you_can
sylvain@ubuntu$ ./67-stop_me_if_you_can
sylvain@ubuntu$
```

- I started 7-highlander in Terminal #0 and then run 67-stop_me_if_you_can in terminal #1, for every iteration we can see I am invincible!!! appearing in terminal #0.

### 8. Beheaded process

Write a Bash script that kills the process 7-highlander.

Terminal #0

```bash
sylvain@ubuntu$ ./7-highlander
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Killed
sylvain@ubuntu$
```

Terminal #1

```bash
sylvain@ubuntu$ ./8-beheaded_process
sylvain@ubuntu$
```

- I started 7-highlander in Terminal #0 and then run 8-beheaded_process in terminal #1 and we can see that the 7-highlander has been killed.

### 9. Process and PID file       #advanced

Write a Bash script that:

- Creates the file /var/run/myscript.pid containing its PID
- Displays To infinity and beyond indefinitely
- Displays I hate the kill command when receiving a SIGTERM signal
- Displays Y U no love me?! when receiving a SIGINT signal
- Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal

```bash
sylvain@ubuntu$ sudo ./100-process_and_pid_file
To infinity and beyond
Terminal #0
To infinity and beyond
^CY U no love me?!
```

Executing the 100-process_and_pid_file script and killing it with ctrl+c.


```bash
sylvain@ubuntu$ sudo ./100-process_and_pid_file
To infinity an
nity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
I hate the kill command
sylvain@ubuntu$ 
```

Terminal #1

```bash
sylvain@ubuntu$ sudo pkill -f 100-process_and_pid_file
sylvain@ubuntu$
```

### 10. Manage my process

Read:

- [&](https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html)
- [init.d](https://www.ghacks.net/2009/04/04/get-to-know-linux-the-etcinitd-directory/)
- [Daemon](https://en.wikipedia.org/wiki/Daemon_%28computing%29)
- [Positional parameters](https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html)

# Manage My Process

## Overview

Programs that run in the background, detached from the terminal, are referred to as daemons or processes. These processes often require management tasks such as starting, restarting, and stopping. On Unix systems, the common approach is to use init scripts for this purpose.

In this project, we provide a Bash script named `manage_my_process` that indefinitely writes "I am alive!" to the file `/tmp/my_process` with a 2-second pause between each message. Additionally, we include an init script, `101-manage_my_process`, to manage the execution of `manage_my_process`. Both scripts should be pushed to the Git repository.

## manage_my_process Bash Script

The `manage_my_process` Bash script performs the following tasks:

- Indefinitely writes "I am alive!" to the file `/tmp/my_process`.
- Pauses for 2 seconds between each "I am alive!" message.

## 101-manage_my_process Init Script

The `101-manage_my_process` init script manages the execution of `manage_my_process`. It supports the following commands:

- `start`: Starts `manage_my_process`, creates a file containing its PID in `/var/run/my_process.pid`, and displays "manage_my_process started."
- `stop`: Stops `manage_my_process`, deletes the file `/var/run/my_process.pid`, and displays "manage_my_process stopped."
- `restart`: Stops `manage_my_process`, deletes the file `/var/run/my_process.pid`, starts `manage_my_process`, creates a file containing its PID in `/var/run/my_process.pid`, and displays "manage_my_process restarted."

Additionally, the script displays "Usage: manage_my_process {start|stop|restart}" if any other argument or no argument is passed.

**Note:** This init script has room for improvement. For example, it does not check if a process is already running when starting. In such a case, it will create a new process instead of indicating that it is already started.

## Requirements

- Both scripts should be pushed to the Git repository.
- The init script should support the commands `start`, `stop`, and `restart`.
- Properly handle PID file creation and deletion.
- Display appropriate messages for the script's status.
- Provide a usage message for incorrect or missing commands.

```bash
sylvain@ubuntu$ sudo ./101-manage_my_process
Usage: manage_my_process {start|stop|restart}
sylvain@ubuntu$ sudo ./101-manage_my_process start
manage_my_process started
sylvain@ubuntu$ tail -f -n0 /tmp/my_process
I am alive!
I am alive!
I am alive!
I am alive!
^C
sylvain@ubuntu$ sudo ./101-manage_my_process stop
manage_my_process stopped
sylvain@ubuntu$ cat /var/run/my_process.pid
cat: /var/run/my_process.pid: No such file or directory
sylvain@ubuntu$ tail -f -n0 /tmp/my_process
^C
sylvain@ubuntu$ sudo ./101-manage_my_process start
manage_my_process started
sylvain@ubuntu$ cat /var/run/my_process.pid
11864
sylvain@ubuntu$ sudo ./101-manage_my_process restart
manage_my_process restarted
sylvain@ubuntu$ cat /var/run/my_process.pid
11918
sylvain@ubuntu$ tail -f -n0 /tmp/my_process
I am alive!
I am alive!
I am alive!
^C
sylvain@ubuntu$
```

### 11. Zombie

Read [what a zombie process is](https://zombieprocess.wordpress.com/what-is-a-zombie-process/).

Write a C program that creates 5 zombie processes.

## Requirements:

- For every zombie process created, it displays Zombie process created, PID: ZOMBIE_PID
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- When your code is done creating the parent process and the zombies, use the function bellow

```C
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
```

## Example:

Terminal #0

``` bash
sylvain@ubuntu$ gcc 102-zombie.c -o zombie
sylvain@ubuntu$ ./zombie
Zombie process created, PID: 13527
Zombie process created, PID: 13528
Zombie process created, PID: 13529
Zombie process created, PID: 13530
Zombie process created, PID: 13531
^C
sylvain@ubuntu$
```

Terminal #1

``` bash
sylvain@ubuntu$ ps aux | grep -e 'Z+.*<defunct>'
sylvain  13527  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
sylvain  13528  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
sylvain  13529  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
sylvain  13530  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
sylvain  13531  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
sylvain  13533  0.0  0.1  10460   964 pts/2    S+   01:19   0:00 grep --color=auto -e Z+.*<defunct>
sylvain@ubuntu$
```

In Terminal #0, I start by compiling 102-zombie.c and executing zombie which creates 5 zombie processes. In Terminal #1, I display the list of processes and look for lines containing Z+.*<defunct> which catches zombie process.
