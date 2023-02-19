import os
import sys
import subprocess
import platform
import colorama as ca
import keyboard as k
from time import sleep
from colorama import Fore as F

ca.init()
os.system('title Roblox Utils')
def tasklist():
    list_task = []
    for support_code_page in ('utf-8', 'cp950', 'cp932'):
        try:
            list_task = subprocess.check_output('tasklist /nh /fo csv').decode(support_code_page).split('\n')[1:-1]
        except:
            continue
    if len(list_task) == 0:
        return None
    for string_proc in list_task:
        try:
            list_proc = eval('[' + string_proc + ']')
        except:
            continue
        exe = list_proc[1]
        return exe


def leave():
    print("Press any key to exit..")
    k.on_press(sys.exit(0))

tasks: list = []

tempdel: str = '''
@echo off
color 0a

if exist "%userprofile%\Desktop\log\" (
    echo.

goto main
) else (
    mkdir "%userprofile%\Desktop\log"
    goto main
)

:main
set /P c="Are you sure you want to clear your temp folder? [Y/N]: "
if "%c%"=="y" (
    goto start
)
if "%c%"=="n" (
    goto exit
)

:start
cd %temp%

:: roblox temp deletion
del /s /f /q RBX* > "%userprofile%\Desktop\log\delete-log.log"
del /s /f /q Roblox > "%userprofile%\Desktop\log\delete-folder-or-file.log"
rmdir /s /q RBX* > "%userprofile%\Desktop\log\delete-folder2.log"

:: other temp deletion
del /s /f /q *.log > "%userprofile%\Desktop\log\delete-log-text.log"
del /s /f /q *.tmp > "%userprofile%\Desktop\log\delete-tmp-file.log"
echo Finished
goto exit

:exit
echo.
echo k, bye
color 07
cd "%userprofile%\Desktop"
EXIT /B 0
'''

def run(prog):
    if ".py" in prog:
        os.system(f'python {prog}')
        return
    if ".bat" in prog:
        os.system(prog)
        return
    os.system(f'./{prog}')

def main():
    print(f'''
{F.RED}Roblox Utils{F.RESET}
{F.BLUE}Welcome, {F.RED}{platform.node()}{F.RESET}

----- Modes -----

1. Temp Delete 
2. Obfuscator
3. Manual Obfuscator
4. hackerman (cool)
5. NoVPN (bad vpn!1!!)
6. Spammer (lol)
''')
    mode: int = int(input("Enter mode: "))
    if mode == 1:
        if os.path.isfile(f"{os.getcwd()}\\rbx-tempdel.bat") != True:
            print('Temp deletion file not found. Creating file, please wait.')
            with open('rbx-tempdel.bat', 'w') as t:
                t.write(tempdel)
            print('\n')
            run('rbx-tempdel.bat')
        if os.path.isfile(f"{os.getcwd()}\\rbx-tempdel.bat"): print('\n'); run("rbx-tempdel.bat")
        leave()
    if mode == 2:
        os.system('start https://luaobfuscator.com')
    if mode == 3:
        if os.path.isfile(f"{os.getcwd()}\\obfuscator.lua") != True:
            with open('obfuscator.lua', 'w') as o:
                o.write('''
local thing = [[
-- Put script here
]]

local encoded = thing:gsub(".", function(bb) return "\\" .. bb:byte() end) or thing .. "\""

-- Credits: https://glot.io/snippets/f1tt9okm5w
print(encoded)''')
        os.system("start 'notepad {os.getcwd()}\\obfuscator.lua'")
        leave()
    if mode == 4:
        os.system('cls')
        print('\nhaha get troll noob')
        sleep(3)
        sys.exit(1)
    if mode == 5:
        tasks.append(tasklist())
        for task in tasks:
            if "VPN" or "vpn" in task:
                os.system('taskkill /f /im {task}')
        leave()
    if mode == 6:
        print("Start: X | you cant stop it manually, you have to wait until it finish")
        message: str = str(input("Enter spam message: "))
        print("\nPlease click on the roblox chatbox, beginning spam in 5 seconds")
        sleep(5)
        for _ in range(15):
            k.type(message)
            sleep(4)
        leave()


if __name__ == "__main__":
    main()

