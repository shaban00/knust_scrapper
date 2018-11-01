#!/usr/bin/evn python
import os
import sys
import time

def banner():

	banner_1 = '''\033[94m
		 /$$   /$$ /$$   /$$ /$$   /$$  /$$$$$$  /$$$$$$$$
		| $$  /$$/| $$$ | $$| $$  | $$ /$$__  $$|__  $$__/
		| $$ /$$/ | $$$$| $$| $$  | $$| $$  \__/   | $$   
		| $$$$$/  | $$ $$ $$| $$  | $$|  $$$$$$    | $$   
		| $$  $$  | $$  $$$$| $$  | $$ \____  $$   | $$   
		| $$\  $$ | $$\  $$$| $$  | $$ /$$  \ $$   | $$   
		| $$ \  $$| $$ \  $$|  $$$$$$/|  $$$$$$/   | $$   
		|__/  \__/|__/  \__/ \______/  \______/    |__/  \033[0m 

\033[92m
  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
 /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$| $$__  $$| $$__  $$| $$_____/| $$__  $$
| $$  \__/| $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$ | $$      | $$$$$$$/| $$$$$$$$| $$$$$$$/| $$$$$$$/| $$$$$   | $$$$$$$/
 \____  $$| $$      | $$__  $$| $$__  $$| $$____/ | $$____/ | $$__/   | $$__  $$
 /$$  \ $$| $$    $$| $$  \ $$| $$  | $$| $$      | $$      | $$      | $$  \ $$
|  $$$$$$/|  $$$$$$/| $$  | $$| $$  | $$| $$      | $$      | $$$$$$$$| $$  | $$
 \______/  \______/ |__/  |__/|__/  |__/|__/      |__/      |________/|__/  |__/
\033[0m
'''

	print(banner_1)


def clear():
	if os.name == "posix":
		os.system("clear")
	elif os.name == "nt":
		os.system("cls")
	elif os.name == "darwin":
		os.system("clear")
	else:
		os.system("clear")


def mainchoice():
	print("+------------------------------------------------------------------------+")
	print("+                                                                        +")
	print("+	\033[91m\033[1m\033[4mUndergraduate\033[0m\033[0m\033[0m                                                    +")
	print("+                                                                        +")
	print("+ 1. International Applicants                                            +")
	print("+ 2. SSSCE/WASSCE Applicants                                             +")
	print("+ 3. Fee paying Applicants(SSSCE/WASSCE)                                 +")
	print("+ 4. Mature/Other/Ghanaian with foreign results Applicants               +")
	print("+ 5. Fee paying Applicants (Mature/Other/Ghanaian with foreign results)  +")
	print("+ 6. NMTC Upgrade Applicants                                             +")
	print("+                                                                        +")
	print("+	\033[91m\033[1m\033[4mPostgraduate\033[0m\033[0m\033[0m                                                     +")
	print("+                                                                        +")
	print("+ 7. International Applicants                                            +")
	print("+ 8. Ghanaian Applicants                                                 +")
	print("+                                                                        +")
	print("+ 99. Exit                                                               +")
	print("+                                                                        +")
	print("+------------------------------------------------------------------------+")