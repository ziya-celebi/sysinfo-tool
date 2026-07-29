import subprocess
# System Information Tool
# A CLI tool to display various system information including logs, hardware, and system details.

def journal_info():
    # Display system journal logs with configurable boot and priority filters.
    boot_choice= input('Enter a boot number between 0-10\n0: current boot\n1: 1 boot ago\n10: 10 boots ago\n')
    priority_choice= input('Enter log priority level between 0-7\n 0: Highest priority\n7: Lowest priority\n')
    subprocess.run(['journalctl', '-b', f'-{boot_choice}', '-p', f'{priority_choice}'])

def ram_info():
    # Display RAM memory usage in human-readable format.
    subprocess.run(['free', '-h'])

def uptime_info():
    # Display system uptime and load averages.
    subprocess.run(['uptime'])

def locale_info():
    # Display current locale settings.
    subprocess.run(['locale'])

def hostname_info():
    # Display system hostname.
    subprocess.run(['hostname'])

def kernel_info():
    # Display kernel version information.
    subprocess.run(['uname', '-r'])

def whoami_info():
    # Display current username.
    subprocess.run(['whoami'])

def lsblk_info():
    # Display block device information with filesystem details.
    subprocess.run(['lsblk', '-f'])

def clear():
    # Clear the terminal screen.
    subprocess.run(['clear'])

def main_loop():
    # Main menu loop that displays options and handles user input.
    clear()
    menu_choice= input('\n1: journal\n2: ram info\n3: uptime\n4: locale\n5: hostname\n6: kernel\n7: whoami\n8: lsblk\n9: exit\n')
    if menu_choice=='1':
        journal_info()
    elif menu_choice=='2':
        ram_info()
    elif menu_choice=='3':
        uptime_info()
    elif menu_choice=='4':
        locale_info()
    elif menu_choice=='5':
        hostname_info()
    elif menu_choice=='6':
        kernel_info()
    elif menu_choice=='7':
        whoami_info()
    elif menu_choice=='8':
        lsblk_info()
    elif menu_choice=='9':
        return False
    else:
        print('invalid')

    input('press enter to return to menu')
    
# Main program loop - continues until user selects exit option
while True:
    if main_loop()== False:
        break
