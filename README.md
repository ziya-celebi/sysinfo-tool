# sysinfo-tool

A simple command-line tool for viewing system information including journal logs, system resources, and hardware details.

## Description

sysinfo-tool provides an interactive menu interface for querying various system information. It allows users to view journal logs, RAM usage, system uptime, locale settings, hostname, kernel version, current user, and block device information.

## Features

- Interactive menu-based interface
- View systemd journal logs with filtering by boot number and priority level
- Display RAM usage information
- Show system uptime
- View locale settings
- Display hostname
- Show kernel version
- Display current user
- List block devices
- Simple and intuitive command-line usage

## Requirements

- Python 3.x
- Linux operating system

## Installation

No installation required. Simply clone or download the repository:

```bash
git clone https://github.com/ziya-celebi/sysinfo-tool.git
cd sysinfo-tool
```

## Usage

Run the tool using Python:

```bash
python3 main.py
```

### Menu Options

Once the tool is running, you'll see the following menu:

```
1: journal
2: ram info
3: uptime
4: locale
5: hostname
6: kernel
7: whoami
8: lsblk
9: exit
```

### Journal Tool Options

When you select option 1, you'll be prompted for:

1. **Boot Number** (0-10):
   - 0: Current boot
   - 1: 1 boot ago
   - 10: 10 boots ago

2. **Log Priority Level** (0-7):
   - 0: Highest priority (emergency)
   - 1: Alert
   - 2: Critical
   - 3: Error
   - 4: Warning
   - 5: Notice
   - 6: Informational
   - 7: Lowest priority (debug)

## Example

```
$ python3 main.py

1: journal
2: ram info
3: uptime
4: locale
5: hostname
6: kernel
7: whoami
8: lsblk
9: exit
1
Enter a boot number between 0-10
0: current boot
1: 1 boot ago
10: 10 boots ago
0
Enter log priority level between 0-7
 0: Highest priority
7: Lowest priority
3
```

This will display error-level and higher priority logs from the current boot.

## How It Works

The tool uses the following system commands:

- `journalctl`: View systemd journal logs
  - `-b`: Specifies the boot number
  - `-p`: Sets the priority level filter
- `free`: Display RAM usage (`-h` for human-readable format)
- `uptime`: Show system uptime
- `locale`: Display locale settings
- `hostname`: Show system hostname
- `uname`: Display kernel information (`-r` for kernel release)
- `whoami`: Show current user
- `lsblk`: List block devices (`-f` for filesystem information)

## License

See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues and enhancement requests.