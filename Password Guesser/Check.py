import os
import colorama
import time
from colorama import just_fix_windows_console
just_fix_windows_console()
from colorama import Fore, Back, Style
dir = os.listdir()
Error = False
Argu = False
Ins = False
if not "App.py" in dir:
    print(f"{Fore.RED}[ERRO] Missing App.py")
    Error = True
if not "Arguments.txt" in dir:
    print(f"{Fore.RED}[ERRO] Missing Arguments.txt")
    Argu = True
if not "Install.bat" in dir:
    print(f"{Fore.RED}[ERRO] Missing Install.bat")
    Ins = True
    Error = True
if not "Run.bat" in dir:
    print(f"{Fore.RED}[ERRO] Missing Run.bat")
    Error = True
if not "Help.txt" in dir:
    print(f"{Fore.RED}[ERRO] Missing Help.txt")
    Error = True
if not "!WIPE.bat" in dir:
    print(f"{Fore.RED}[ERRO] Missing !WIPE.bat")
    Error = True
if not "Wipe.py" in dir:
    print(f"{Fore.RED}[ERRO] Missing Wipe.py")
    Error = True
if Error:
    print(f"{Fore.CYAN}[INFO] {Fore.RESET}Please reinstall Password Guesser Englishexe v1 from 'link', you might be "
          f"using a outdated or corrupt version")
else:
    print(f"{Fore.GREEN}[OKAY] {Fore.RESET}No issues found, reinstall Password Guesser Englishexe v1 if a error "
          "Occurs")
if Argu:
    if not Ins:
        print(f"{Fore.GREEN}[OKAY] {Fore.RESET}Installing Arguments.txt")
        os.system("Install.bat")
    else:
        print(f"{Fore.RED}[Warn] Impossible to install Arguments.txt, follow instructions above.")
if Error:
    input("Press ENTER to continue (Not suggested)")
