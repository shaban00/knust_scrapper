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
#6. NMTC Upgrade : https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=15&streamid=13&page=1         total_pages=21

#-----------------------
#Postgraduate Applicants
#-----------------------
#1. International Applicants : https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=11&streamid=2&page=1         total_pages=4
#2. Ghanaian Applicants : https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=12&streamid=2&page=1         total_pages=54



# Import requests
try:
	import requests
	from requests import ConnectionError
except ImportError:
	print("Warning: missing package 'requests' is required")
# Import bs4
try:
	from bs4 import BeautifulSoup
except ImportError:
	print("Warning: missing package 'bs4' is required")
	print("Fix: 'sudo pip install -r requirements.txt'")
	sys.exit(1)


# Base url for website
base_url = "https://apps.knust.edu.gh/admissions/check/Home/"

# List of students path urls
students_urls = [
		"ApplicantList?offer=9&streamid=1&page=",
		"ApplicantList?offer=1&streamid=1&page=",
		"ApplicantList?offer=3&streamid=1&page=",
		"ApplicantList?offer=8&streamid=1&page=",
		"ApplicantList?offer=10&streamid=1&page=",
		"ApplicantList?offer=15&streamid=13&page=",
		"ApplicantList?offer=11&streamid=2&page=",
		"ApplicantList?offer=12&streamid=2&page"
]


def students_scrapper(url, end, filename):

	if not os.path.exists(filename):
		os.mknod(filename)

	csvFile = open(filename, "wt+")
	writer = csv.writer(csvFile)

	try:
		print("\033[93m[+] Loading...(Please wait)\033[0m")
		for i in range(1, end+1):
			# url of pages
			full_url = url + "{}".format(i)

			req = requests.get(full_url)
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

			full_url = url

	except ConnectionError:
		print("\033[91m[-]\033[0m Problem connecting to {}".format(base_url))

		if os.path.exists(filename):
				os.remove(filename)

	print("\n\033[92m[*]\033[0m Done...")	
	
	if os.path.exists(filename):
		csvFile.close()


def main():

	clear()
	banner()

	myLoop = True
	mainchoice()

	while myLoop:

		choice = int(input("\033[92mchoice>>\033[0m "))
		if choice == 1:
			url = students_urls[0]
			url = base_url + url
			end = 4
			filename = "students1.csv"
			students_scrapper(url, end, filename)
			myLoop = False

		elif choice == 2:
			url = students_urls[1]
			url = base_url + url
			end = 328
			filename = "students2.csv"
			students_scrapper(url, end, filename)
			myLoop = False

		elif choice == 3:
			url = students_urls[2]
			url = base_url + url
			end = 135
			filename = "students3.csv"
			students_scrapper(url, end, filename)
			myLoop = False

		elif choice == 4:
			url = students_urls[3]
			url = base_url + url
			end = 2
			filename = "students4.csv"
			students_scrapper(url, end, filename)
			myLoop = False

		elif choice == 5:
			url = students_urls[4]
			url = base_url + url
			end = 9
			filename = "students5.csv"
			students_scrapper(url, end, filename)
			myLoop = False

		elif choice == 6:
			url = students_urls[5]
			url = base_url + url
			end = 21
			filename = "students6.csv"
			students_scrapper(url, end, filename)
			myLoop = False

		elif choice == 7:
			url = students_urls[6]
			url = base_url + url
			end = 4
			filename = "students7.csv"
			students_scrapper(url, end, filename)
			myLoop = False

		elif choice == 8:
			url = students_urls[7]
			url = base_url + url
			end = 54
			filename = "students8.csv"
			students_scrapper(url, end, filename)
			myLoop = False

		elif choice == 99:
			print("\033[92m[*]\033[0m Exiting...")
			time.sleep(1)
			sys.exit(1)

		else:
			clear()
			mainchoice()

if __name__ == '__main__':
	main()
