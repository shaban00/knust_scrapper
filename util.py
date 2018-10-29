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
		None

def animate():
	while True:
		sys.stdout.write("\r[+] Loading... |")
		time.sleep(0.001)
		sys.stdout.write("\r[+] Loading... /")
		time.sleep(0.001)
		sys.stdout.write("\r[+] Loading... -")
		time.sleep(0.001)
		sys.stdout.write("\r[+] Loading... \\")
		time.sleep(0.001)
	sys.stdout.write("\r[+] Done...")


def python_version():
	version = sys.version[:5].split(".")[0]
	return version

def progress2():
        toolbar_width = 50

        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width + 1))

        for i in range(toolbar_width):
                time.sleep(0.1)
                sys.stdout.write("#")
                sys.stdout.flush()
        sys.stdout.write("\n")



def mainchoice():
	print("+------------------------------------------------------------------------+")
	print("+                                                                        +")
	print("+ 1. Undergraduate                                                       +")
	print("+ 2. Postgraduate                                                        +")
	print("+ 3. Distance Learning                                                   +")
	print("+ 99. Exit                                                               +")
	print("+                                                                        +")
	print("+------------------------------------------------------------------------+")

def undergraduate():
	print("+------------------------------------------------------------------------+")
	print("+                                                                        +")
	print("+*******Undergraduate********                                            +")
	print("+                                                                        +")
	print("+ 1. International Applicants                                            +")
	print("+ 2. SSSCE/WASSCE Applicants                                             +")
	print("+ 3. Fee paying Applicants(SSSCE/WASSCE)                                 +")
	print("+ 4. Mature/Other/Ghanaian with foreign results Applicants               +")
	print("+ 5. Fee paying Applicants (Mature/Other/Ghanaian with foreign results)  +")
	print("+ 6. Applicants from Less Endowed Schools                                +")
	print("+ 7. NMTC Upgrade Applicants                                             +")
	print("+                                                                        +")
	print("+*******Postgraduate********                                             +")
	print("+                                                                        +")
	print("+ 8. International Applicants                                            +")
	print("+ 9. Ghanaian Applicants                                                 +")
	print("+                                                                        +")
	print("+*******Distance Learning********                                        +")
	print("+                                                                        +")
	print("+ 10. Diploma Applicants                                                  +")
	print("+ 11. Undergraduate Applicants                                            +")
	print("+ 12. Postgraduate Applicants                                             +")
	print("+                                                                        +")
	print("+ 99. Exit                                                               +")
	print("+                                                                        +")
	print("+------------------------------------------------------------------------+")

def postgraduate():
	print("+------------------------------------------------------------------------+")
	print("+                                                                        +")
	print("+*******Undergraduate********                                            +")
	print("+                                                                        +")
	print("+ 1. International Applicants                                            +")
	print("+ 2. Ghanaian Applicants                                                 +")
	print("+ 99. Back                                                               +")
	print("+                                                                        +")
	print("+------------------------------------------------------------------------+")

def distancelearning():
	print("+------------------------------------------------------------------------+")
	print("+                                                                        +")
	print("+ 1. Diploma Applicants                                                  +")
	print("+ 2. Undergraduate Applicants                                            +")
	print("+ 3. Postgraduate Applicants                                             +")
	print("+ 99. Back                                                               +")
	print("+                                                                        +")
	print("+------------------------------------------------------------------------+") 
