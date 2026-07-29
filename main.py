import subprocess

while True:
    boot_choice= input('Enter a boot number between 0-10\n0: current boot\n1: 1 boot ago\n10: 10 boots ago\n')
    priority_choice= input('Enter log priority level between 0-7\n 0: Highest priority\n7: Lowest priority\n')
    subprocess.run(['journalctl', '-b', f'-{boot_choice}', '-p', f'{priority_choice}'])
  




