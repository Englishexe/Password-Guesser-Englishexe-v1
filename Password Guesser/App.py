# Copyright Disclaimer:
# Using this program normally falls under teaching This content is made for "fair use" for
# purposes such as criticism, comment, news reporting, teaching, scholarship and research.
# Fair use is a use permitted by copyright statute that might otherwise be infringing.
# (Section 107 of the Copyright Act 1976)

print("[----] ---------------")
print("[OKAY] Started python")
print("[OKAY] Starting imports")
import os
import time
import colorama
import sys
import random
from colorama import just_fix_windows_console

just_fix_windows_console()
from colorama import Fore, Back, Style

print(f"{Fore.GREEN}[OKAY]{Fore.RESET} Started imports")
print(f"{Fore.GREEN}[OKAY]{Fore.RESET} Starting dir")
print(f"{Fore.GREEN}[OKAY]{Fore.RESET} Checking arguments")
if "-Clean" in sys.argv:
    Clean = True
else:
    Clean = False
if "-Noinfo" in sys.argv:
    Info = False
else:
    Info = True
if "-Debug" in sys.argv:
    Debug = True
else:
    Debug = False
if Debug:
    print(f"{Fore.RED}[DEBU] {Fore.RESET}{os.listdir()}")
    print(f"{Fore.RED}[DEBU] {Fore.RESET}{sys.argv}")
    print(f"{Fore.RED}[DEBU] {Fore.RESET}Clean:{Clean}")
    print(f"{Fore.RED}[DEBU] {Fore.RESET}Info:{Info}")
    print(f"{Fore.RED}[DEBU] {Fore.RESET}Debug:{Debug}")
if not "passwords" in os.listdir():
    print(f"{Fore.YELLOW}[MAKE]{Fore.RESET} No passwords dir, making one...")
    os.mkdir("passwords")
os.chdir("passwords")
print(f"{Fore.GREEN}[OKAY]{Fore.RESET} Started dir and entered dir")

print(f"{Fore.GREEN}[OKAY] Initialised ")
if Clean:
    os.system("cls")
print(f"{Fore.WHITE}Made by Englishexe - Password Guesser Englishexe v1")
if Info:
    print("-----------")
    print(f"{Fore.CYAN}[INFO]{Fore.RESET} Color codes:")
    print(f"{Fore.CYAN}[INFO]{Fore.YELLOW} [WARN] {Fore.WHITE}Warnings will appear like this")
    print(f"{Fore.CYAN}[INFO]{Fore.RED} [ERRO] Errors will appear like this")
    print(f"{Fore.CYAN}[INFO]{Fore.CYAN} [INFO] {Fore.WHITE}Info will appear like this")
    print(f"{Fore.CYAN}[INFO]{Fore.GREEN} [OKAY] {Fore.WHITE}Logs / Successful alerts will appear like this")
    print(
        f"{Fore.CYAN}[INFO]{Fore.MAGENTA} [USER] {Fore.WHITE}Inputs will appear like this{Fore.CYAN} User text{Fore.RESET}")
    print(f"{Fore.CYAN}[INFO]{Fore.RESET} Disable this by adding -Noinfo to Arguments.txt")
    print(f"{Fore.CYAN}[INFO]{Fore.RESET} ")
    print("-----------")
if Info:
    print(f"{Fore.CYAN}[INFO] {Fore.RESET}Ideas for names : John Doe's amazon")
Guess_Name = input(f"{Fore.MAGENTA}[USER] {Fore.RESET}Name this guess:{Fore.CYAN}")
print(f"{Fore.GREEN}[OKAY]{Fore.RESET} Name set to '{Fore.CYAN}{Guess_Name}{Fore.RESET}'")
if Debug:
    print(f"{Fore.RED}[DEBU] {Fore.RESET}{Guess_Name}")
if Info:
    print(
        f"{Fore.CYAN}[INFO] {Fore.CYAN}[{Guess_Name}] {Fore.RESET}Ideas for username/email/pn : {os.getlogin()}, 01234567890")
Guess_Login = input(
    f"{Fore.MAGENTA}[USER] {Fore.CYAN}[{Guess_Name}] {Fore.RESET}What is the account username/email/phone number:{Fore.CYAN}")
print(
    f"{Fore.GREEN}[OKAY] {Fore.CYAN}[{Guess_Name}] [{Guess_Login}] {Fore.RESET}User/Email/PN set to: '{Fore.CYAN}{Guess_Login}{Fore.RESET}'")
if Debug:
    print(f"{Fore.RED}[DEBU] {Fore.RESET}{Guess_Login}")
print(f"{Fore.GREEN}[OKAY] {Fore.CYAN}[{Guess_Name}] [{Guess_Login}] {Fore.RESET}Creating files")
if not Guess_Name in os.listdir():
    os.mkdir(Guess_Name)
else:
    print(f"{Fore.YELLOW}[WARN] {Fore.CYAN}[{Guess_Name}] [{Guess_Login}] {Fore.RESET}{Guess_Name} already exists, "
          f"destroying old files...")
os.chdir(Guess_Name)
f = open("Username,email,pn.txt", "w")
f.write(Guess_Login)
f.close()
f = open("Passwords.dat", "w")
f.write(f"Passwords.dat-{os.getlogin()}")
f.close()
f = open("Info.txt", "w")
f.write(f"Info.txt-{os.getlogin()}")
f.close()
f = open("Passwords.dat", "a")
f.write("\n")
f.write(f"Passwords.dat made by {os.getlogin()} automatically using 'Password Guesser Englishexe v1'")
f.write("\n")
f.write("By using these passwords you intend no malicious intent and take full responsibility")
f.close()
f = open("info.txt", "a")
f.write("\n")
f.write(f"info.txt made by {os.getlogin()} automatically using 'Password Guesser Englishexe v1'")
f.write("\n")
f.write("Info would go here but there is none?")
f.close()
print(f"{Fore.GREEN}[OKAY] {Fore.CYAN}[{Guess_Name}] [{Guess_Login}] {Fore.RESET}Created files")
if Info:
    print(f"{Fore.CYAN}[INFO] {Fore.RESET}Add info like names, significant dates. Separated by commas")
Sig = input(f"{Fore.MAGENTA}[USER] {Fore.CYAN}[{Guess_Name}] [{Guess_Login}] {Fore.RESET}Significant info:{Fore.CYAN}")
Sig = Sig.replace(" ", "")
Guesses = Sig.split(",")
if Debug:
    print(f"{Fore.RED}[DEBU] {Fore.RESET}{Guesses}")
print(f"{Fore.RED}[ERRO] This program has been discontinued due to security reasons.")
input(f"{Fore.YELLOW}End of script, no further lines.")
