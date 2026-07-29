import subprocess

def journal():
    boot_choice= input('Enter a boot number between 0-10\n0: current boot\n1: 1 boot ago\n10: 10 boots ago\n')
    priority_choice= input('Enter log priority level between 0-7\n 0: Highest priority\n7: Lowest priority\n')
    subprocess.run(['journalctl', '-b', f'-{boot_choice}', '-p', f'{priority_choice}'])

def main_loop():
    menu_choice= input('1: journal-tool\n2: exit\n')
    if menu_choice=='1':
        journal()
    elif menu_choice=='2':
        return False
    else:
        print('invalid')

while True:
    if main_loop()== False:
        break
