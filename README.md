# sysinfo-tool

A simple command-line tool for viewing systemd journal logs with filtering capabilities.

## Description

sysinfo-tool provides an interactive menu interface for querying systemd journal logs. It allows users to filter logs by boot number and priority level, making it easier to troubleshoot system issues across different boot sessions.

## Features

- Interactive menu-based interface
- Filter journal logs by boot number (0-10)
- Filter logs by priority level (0-7)
- Simple and intuitive command-line usage

## Requirements

- Python 3.x
- systemd (for `journalctl` command)
- Linux operating system with systemd init system

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
1: journal-tool
2: exit
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

1: journal-tool
2: exit
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

The tool uses the `journalctl` command with the following flags:
- `-b`: Specifies the boot number
- `-p`: Sets the priority level filter

## License

See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues and enhancement requests.