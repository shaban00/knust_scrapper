#!/usr/bin/env python

import csv
from util import *
import os
import sys
import time

#-------------------------
#Undergraduates Applicants
#-------------------------
#1. International Applicants : https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=9&streamid=1&page=1         total_pages=4
#2. SSSCE/WASSCE Applicants : https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=1&streamid=1&page=1         total_pages=328
#3. Fee paying Applicants(SSSCE/WASSCE) : https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=3&streamid=1&page=1         total_pages=135
#4. Mature/Other/Ghanaian with foreign results Applicants : https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=8&streamid=1&page=1         total_pages=2
#5. Fee paying Applicants (Mature/Other/Ghanaian with foreign results) : https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=10&streamid=1&page=1         total_pages=9
#6. Applicants from Less Endowed Schools : https://apps.knust.edu.gh/admissions/check/Home/LessEndowed?page=1         total_pages=33
#7. NMTC Upgrade : https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=15&streamid=13&page=1         total_pages=21

#-----------------------
#Postgraduate Applicants
#-----------------------
#1. International Applicants : https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=11&streamid=2&page=1         total_pages=4
#2. Ghanaian Applicants : https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=12&streamid=2&page=1         total_pages=54

#----------------
#Distance Learning Applicants
#1. Diploma Applicants : https://apps.knust.edu.gh/admissions/check/Home/Distance?group=35&page=1         total_pages=20
#2. Undergraduate Applicants : https://apps.knust.edu.gh/admissions/check/Home/Distance?group=5&page=1         total_pages=44
#3. Postgraduate Applicants : https://apps.knust.edu.gh/admissions/check/Home/Distance?group=6&page=1         total_pages=69
#--------------



try:
	import requests
	from requests import ConnectionError
	from requests import ConnectTimeout
except ImportError:
	print("Warning: missing package 'requests' is required")

try:
	from bs4 import BeautifulSoup
except ImportError:
	print("Warning: missing package 'bs4' is required")
	print("Fix: 'sudo pip install -r requirements.txt'")
	sys.exit(1)


base_url = "https://apps.knust.edu.gh/"
student_directory= "admissions/check/Home/"

status_code = requests.get(base_url).status_code
if status_code == 200:
	None
else:
	print("{} is down...".format(base_url))
	sys.exit(1)


students_urls = [
		"ApplicantList?offer=9&streamid=1&page=",
		"ApplicantList?offer=1&streamid=1&page=",
		"ApplicantList?offer=3&streamid=1&page=",
		"ApplicantList?offer=8&streamid=1&page=",
		"ApplicantList?offer=10&streamid=1&page=",
		"LessEndowed?page=",
		"ApplicantList?offer=15&streamid=13&page=",
		"ApplicantList?offer=11&streamid=2&page=",
		"ApplicantList?offer=12&streamid=2&page",
		"Distance?group=35&page=",
		"Distance?group=5&page=",
		"Distance?group=6&page="
]


def students_scrapper(url, end, filename):
	
	if not os.path.exists(filename):
		os.mknod(filename)

	csvFile = open(filename, "wt+")
	writer = csv.writer(csvFile)

	try:
		print("\033[93m[+] Loading...(Please wait)\033[0m")
		for i in range(1, end, 1):
			url = url + "{}".format(i)

			req = requests.get(url)
			soup = BeautifulSoup(req.text, "html.parser")

			table = soup.find("table")
			rows = table.find_all("tr")
			sys.stdout.write("#")
			sys.stdout.flush()

			try:
				for row in rows:
					csvRow = []
					for cell in row.find_all(["td", "th"]):
						# Correct UnicodeError
						csvRow.append(cell.get_text().encode("ascii", "ignore"))
						
						if len(csvRow) == 4:
							if csvRow[0].isdigit():
								csvRow.pop(0)

								if csvRow[0].isdigit():
									writer.writerow(csvRow)
							else:
								None
						else:
							None
			except Exception as e:
				print("No rows found")

	except ConnectionError:
		print("[-] Problem connecting to {}...".format(base_url))

		if os.path.exists(filename):
				os.remove(filename)

	except ConnectTimeout:
		print("[-] Connection Timeout...")

	print("\n[*] Done...")	
	
	if os.path.exists(filename):
		csvFile.close()


def main():

	mainchoice()

	#choice = int(input("choice>> "))
	choice = str(input("choice>> "))
	if "1" in choice:
		url = students_urls[0]
		url = base_url + student_directory + url
		end = 4
		filename = "students1.csv"
		students_scrapper(url, end, filename)
	if "2" in choice:
		url = students_urls[1]
		url = base_url + student_directory + url
		end = 328
		filename = "students2.csv"
		students_scrapper(url, end, filename)

	if "3" in choice:
		url = students_urls[2]
		url = base_url + student_directory + url
		end = 135
		filename = "students3.csv"
		students_scrapper(url, end, filename)

	if "4" in choice:
		url = students_urls[3]
		url = base_url + student_directory + url
		end = 2
		filename = "students4.csv"
		students_scrapper(url, end, filename)

	if "5" in choice:
		url = students_urls[4]
		url = base_url + student_directory + url
		end = 9
		filename = "students5.csv"
		students_scrapper(url, end, filename)

	if "6" in choice:
		url = students_urls[5]
		url = base_url + student_directory + url
		end = 33
		filename = "students6.csv"
		students_scrapper(url, end, filename)

	if "7" in choice:
		url = students_urls[6]
		url = base_url + student_directory + url
		end = 21
		filename = "students7.csv"
		students_scrapper(url, end, filename)

	if "8" in choice:
		url = students_urls[7]
		url = base_url + student_directory + url
		end = 4
		filename = "students8.csv"
		students_scrapper(url, end, filename)

	if "9" in choice:
		url = students_urls[8]
		url = base_url + student_directory + url
		end = 54
		filename = "students9.csv"
		students_scrapper(url, end, filename)

	if "10" in choice:
		url = students_urls[9]
		url = base_url + student_directory + url
		end = 20
		filename = "students10.csv"
		students_scrapper(url, end, filename)

	if "11" in choice:
		url = students_urls[10]
		url = base_url + student_directory + url
		end = 44
		filename = "students11.csv"
		students_scrapper(url, end, filename)

	if "12" in choice:
		url = students_urls[11]
		url = base_url + student_directory + url
		end = 69
		filename = "students12.csv"
		students_scrapper(url, end, filename)

	elif choice == "99":
		sys.exit(1)

	else:
		print("Invalid selection...")



if __name__ == '__main__':
	main()
