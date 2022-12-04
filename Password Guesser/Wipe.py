import os
from time import sleep
from colorama import just_fix_windows_console
just_fix_windows_console()
from colorama import Fore, Back, Style
Home_Directory = os.listdir()
if not "passwords" in Home_Directory:
    print(f"{Fore.YELLOW}[Warn] {Fore.RESET}No passwords directory, nothing to remove!")
else:
    print(f"{Fore.GREEN}[OKAY] {Fore.RESET}Removing directory")
    os.system("rmdir passwords /S /Q")
    print(f"{Fore.GREEN}[OKAY] {Fore.RESET}Removed directory")


