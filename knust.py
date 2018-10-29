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


base_url = "https://apps.knust.edu/"
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


def main():
	for url in students_urls:
		print(base_url + student_directory + url)


def undergraduate_international_applicants():

	base_url = "https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=9&streamid=1&page="

	if not os.path.exists("Undergraduate-International-Applicants.csv"):
		os.mknod("Undergraduate-International-Applicants.csv")

	csvFile = open("Undergraduate-International-Applicants.csv", "wt+")
	writer = csv.writer(csvFile)

	try:
		print("\033[93m[+] Loading...(Please wait)\033[0m")
		for i in range(1,5,1):
			url = base_url+"{}".format(i)

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
				print("No table rows found")
		print(u"\033[92m\033[1m\n[\u2713] Done\033[0m\033[0m")
	except ConnectionError as e:
		print("[-] Problem connecting to website...")
		print("[-] Exiting...")
		# Remove students.csv file if  exist
		if os.path.exists("Undergraduate-International-Applicants.csv"):
				os.remove("Undergraduate-International-Applicants.csv")

	except ConnectTimeout as c:
		print("[-] Connection Timeout...")
		print("[*] Retrying...")		
	# Close students.csv file if exist
	if os.path.exists("Undergraduate-International-Applicants.csv"):
		csvFile.close()


def undergraduate_ssce_wassce_applicants():

	base_url = "https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=1&streamid=1&page="
	# Create students.csv file if not exist
	if not os.path.exists("Undergraduate-SSSCE-WASSCE-Applicants.csv"):
		os.mknod("Undergraduate-SSSCE-WASSCE-Applicants.csv")
	# Open students.csv file
	csvFile = open("Undergraduate-SSSCE-WASSCE-Applicants.csv", "wt+")
	writer = csv.writer(csvFile)
	
	try:	
		print("\033[93m[+] Loading...(Please wait)\033[0m")	
		# Loop between total number of pages (total=328)
		for i in range(1,329,1):
			url = base_url+"{}".format(i)
			# Make request to site (https://www.knust.edu.gh)
			req = requests.get(url)   
			soup = BeautifulSoup(req.text, "html.parser")
			# Find table on page
			table = soup.find("table")
			# Find all table rows
			rows = table.find_all("tr")
			# Progess bar
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
				print("No table rows found")
		print(u"\033[92m\033[1m\n[\u2713] Done\033[0m\033[0m")
	except ConnectionError as e:
		print("[-] Problem connecting to website...")
		print("[-] Exiting...")
		# Remove students.csv file if  exist
		if os.path.exists("Undergraduate-SSSCE-WASSCE-Applicants.csv"):
				os.remove("Undergraduate-SSSCE-WASSCE-Applicants.csv")

	except ConnectTimeout as c:
		print("[-] Connection Timeout...")
		print("[*] Retrying...")	
	# Close students.csv file if exist
	if os.path.exists("Undergraduate-SSSCE-WASSCE-Applicants.csv"):
		csvFile.close()

def undergraduate_fee_paying_ssce_wassce_applicants():

	base_url = "https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=3&streamid=1&page="
	# Create students.csv file if not exist
	if not os.path.exists("Undergraduate-Fee-Paying-SSSCE-WASSCE-Applicants.csv"):
		os.mknod("Undergraduate-Fee-Paying-SSSCE-WASSCE-Applicants.csv")
	# Open students.csv file
	csvFile = open("Undergraduate-Fee-Paying-SSSCE-WASSCE-Applicants.csv", "wt+")
	writer = csv.writer(csvFile)
	
	try:	
		print("\033[93m[+] Loading...(Please wait)\033[0m")	
		# Loop between total number of pages (total=328)
		for i in range(1,136,1):
			url = base_url+"{}".format(i)
			# Make request to site (https://www.knust.edu.gh)
			req = requests.get(url)   
			soup = BeautifulSoup(req.text, "html.parser")
			# Find table on page
			table = soup.find("table")
			# Find all table rows
			rows = table.find_all("tr")
			# Progess bar
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
				print("No table rows found")
		print(u"\033[92m\033[1m\n[\u2713] Done\033[0m\033[0m")
	except ConnectionError as e:
		print("[-] Problem connecting to website...")
		print("[-] Exiting...")
		# Remove students.csv file if  exist
		if os.path.exists("Undergraduate-Fee-Paying-SSSCE-WASSCE-Applicants.csv"):
				os.remove("Undergraduate-Fee-Paying-SSSCE-WASSCE-Applicants.csv")

	except ConnectTimeout as c:
		print("[-] Connection Timeout...")
		print("[*] Retrying...")	
	# Close students.csv file if exist
	if os.path.exists("Undergraduate-Fee-Paying-SSSCE-WASSCE-Applicants.csv"):
		csvFile.close()

def undergraduate_mature_foreign_applicants():

	base_url = "https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=8&streamid=1&page="
	# Create students.csv file if not exist
	if not os.path.exists("Undergraduate-Mature-Foreign-Applicants.csv"):
		os.mknod("Undergraduate-Mature-Foreign-Applicants.csv")
	# Open students.csv file
	csvFile = open("Undergraduate-Mature-Foreign-Applicants.csv", "wt+")
	writer = csv.writer(csvFile)
	
	try:	
		print("\033[93m[+] Loading...(Please wait)\033[0m")	
		# Loop between total number of pages (total=328)
		for i in range(1,3,1):
			url = base_url+"{}".format(i)
			# Make request to site (https://www.knust.edu.gh)
			req = requests.get(url)   
			soup = BeautifulSoup(req.text, "html.parser")
			# Find table on page
			table = soup.find("table")
			# Find all table rows
			rows = table.find_all("tr")
			# Progess bar
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
				print("No table rows found")
		print(u"\033[92m\033[1m\n[\u2713] Done\033[0m\033[0m")
	except ConnectionError as e:
		print("[-] Problem connecting to website...")
		print("[-] Exiting...")
		# Remove students.csv file if  exist
		if os.path.exists("Undergraduate-Mature-Foreign-Applicants.csv"):
				os.remove("Undergraduate-Mature-Foreign-Applicants.csv")

	except ConnectTimeout as c:
		print("[-] Connection Timeout...")
		print("[*] Retrying...")	
	# Close students.csv file if exist
	if os.path.exists("Undergraduate-Mature-Foreign-Applicants.csv"):
		csvFile.close()

def undergraduate_fee_paying_foreign_applicants():

	base_url = "https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=10&streamid=1&page="
	# Create students.csv file if not exist
	if not os.path.exists("Undergraduate-Fee-Paying-Foreign-Applicants.csv"):
		os.mknod("Undergraduate-Fee-Paying-Foreign-Applicants.csv")
	# Open students.csv file
	csvFile = open("Undergraduate-Fee-Paying-Foreign-Applicants.csv", "wt+")
	writer = csv.writer(csvFile)
	
	try:	
		print("\033[93m[+] Loading...(Please wait)\033[0m")	
		# Loop between total number of pages (total=328)
		for i in range(1,10,1):
			url = base_url+"{}".format(i)
			# Make request to site (https://www.knust.edu.gh)
			req = requests.get(url)   
			soup = BeautifulSoup(req.text, "html.parser")
			# Find table on page
			table = soup.find("table")
			# Find all table rows
			rows = table.find_all("tr")
			# Progess bar
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
				print("No table rows found")
		print(u"\033[92m\033[1m\n[\u2713] Done\033[0m\033[0m")
	except ConnectionError as e:
		print("[-] Problem connecting to website...")
		print("[-] Exiting...")
		# Remove students.csv file if  exist
		if os.path.exists("Undergraduate-Fee-Paying-Foreign-Applicants.csv"):
				os.remove("Undergraduate-Fee-Paying-Foreign-Applicants.csv")

	except ConnectTimeout as c:
		print("[-] Connection Timeout...")
		print("[*] Retrying...")	
	# Close students.csv file if exist
	if os.path.exists("Undergraduate-Fee-Paying-Foreign-Applicants.csv"):
		csvFile.close()

def undergraduate_less_endowed_applicants():

	base_url = "https://apps.knust.edu.gh/admissions/check/Home/LessEndowed?page="
	# Create students.csv file if not exist
	if not os.path.exists("Undergraduate-Less-Endowed-Applicants.csv"):
		os.mknod("Undergraduate-Less-Endowed-Applicants.csv")
	# Open students.csv file
	csvFile = open("Undergraduate-Less-Endowed-Applicants.csv", "wt+")
	writer = csv.writer(csvFile)
	
	try:	
		print("\033[93m[+] Loading...(Please wait)\033[0m")	
		# Loop between total number of pages (total=328)
		for i in range(1,34,1):
			url = base_url+"{}".format(i)
			# Make request to site (https://www.knust.edu.gh)
			req = requests.get(url)   
			soup = BeautifulSoup(req.text, "html.parser")
			# Find table on page
			table = soup.find("table")
			# Find all table rows
			rows = table.find_all("tr")
			# Progess bar
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
								writer.writerow(csvRow)
												
							else:
								None
						else:
							None
			except Exception as e:
				print("No table rows found")
		print(u"\033[92m\033[1m\n[\u2713] Done\033[0m\033[0m")
	except ConnectionError as e:
		print("[-] Problem connecting to website...")
		print("[-] Exiting...")
		# Remove students.csv file if  exist
		if os.path.exists("Undergraduate-Less-Endowed-Applicants.csv"):
				os.remove("Undergraduate-Less-Endowed-Applicants.csv")

	except ConnectTimeout as c:
		print("[-] Connection Timeout...")
		print("[*] Retrying...")	
	# Close students.csv file if exist
	if os.path.exists("Undergraduate-Less-Endowed-Applicants.csv"):
		csvFile.close()

def undergraduate_nmtc_upgrade_applicants():

	base_url = "https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=15&streamid=13&page="
	# Create students.csv file if not exist
	if not os.path.exists("Undergraduate-NMTC-Upgrade-Applicants.csv"):
		os.mknod("Undergraduate-NMTC-Upgrade-Applicants.csv")
	# Open students.csv file
	csvFile = open("Undergraduate-NMTC-Upgrade-Applicants.csv", "wt+")
	writer = csv.writer(csvFile)
	
	try:	
		print("\033[93m[+] Loading...(Please wait)\033[0m")	
		# Loop between total number of pages (total=328)
		for i in range(1,22,1):
			url = base_url+"{}".format(i)
			# Make request to site (https://www.knust.edu.gh)
			req = requests.get(url)   
			soup = BeautifulSoup(req.text, "html.parser")
			# Find table on page
			table = soup.find("table")
			# Find all table rows
			rows = table.find_all("tr")
			# Progess bar
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
				print("No table rows found")
		print(u"\033[92m\033[1m\n[\u2713] Done\033[0m\033[0m")
	except ConnectionError as e:
		print("[-] Problem connecting to website...")
		print("[-] Exiting...")
		# Remove students.csv file if  exist
		if os.path.exists("Undergraduate-NMTC-Upgrade-Applicants.csv"):
				os.remove("Undergraduate-NMTC-Upgrade-Applicants.csv")

	except ConnectTimeout as c:
		print("[-] Connection Timeout...")
		print("[*] Retrying...")	
	# Close students.csv file if exist
	if os.path.exists("Undergraduate-NMTC-Upgrade-Applicants.csv"):
		csvFile.close()

def postgraduate_international_applicants():

	base_url = "https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=11&streamid=2&page="
	# Create students.csv file if not exist
	if not os.path.exists("Postgraduate-International-Applicants.csv"):
		os.mknod("Postgraduate-International-Applicants.csv")
	# Open students.csv file
	csvFile = open("Postgraduate-International-Applicants.csv", "wt+")
	writer = csv.writer(csvFile)
	
	try:	
		print("\033[93m[+] Loading...(Please wait)\033[0m")	
		# Loop between total number of pages (total=328)
		for i in range(1,5,1):
			url = base_url+"{}".format(i)
			# Make request to site (https://www.knust.edu.gh)
			req = requests.get(url)   
			soup = BeautifulSoup(req.text, "html.parser")
			# Find table on page
			table = soup.find("table")
			# Find all table rows
			rows = table.find_all("tr")
			# Progess bar
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
				print("No table rows found")
		print(u"\033[92m\033[1m\n[\u2713] Done\033[0m\033[0m")
	except ConnectionError as e:
		print("[-] Problem connecting to website...")
		print("[-] Exiting...")
		# Remove students.csv file if  exist
		if os.path.exists("Postgraduate-International-Applicants.csv"):
				os.remove("Postgraduate-International-Applicants.csv")

	except ConnectTimeout as c:
		print("[-] Connection Timeout...")
		print("[*] Retrying...")	
	# Close students.csv file if exist
	if os.path.exists("Postgraduate-International-Applicants.csv"):
		csvFile.close()

def postgraduate_ghanaian_applicants():

	base_url = "https://apps.knust.edu.gh/admissions/check/Home/ApplicantList?offer=12&streamid=2&page="
	# Create students.csv file if not exist
	if not os.path.exists("Postgraduate-Ghanaian-Applicants.csv"):
		os.mknod("Postgraduate-Ghanaian-Applicants.csv")
	# Open students.csv file
	csvFile = open("Postgraduate-Ghanaian-Applicants.csv", "wt+")
	writer = csv.writer(csvFile)
	
	try:	
		print("\033[93m[+] Loading...(Please wait)\033[0m")	
		# Loop between total number of pages (total=328)
		for i in range(1,55,1):
			url = base_url+"{}".format(i)
			# Make request to site (https://www.knust.edu.gh)
			req = requests.get(url)   
			soup = BeautifulSoup(req.text, "html.parser")
			# Find table on page
			table = soup.find("table")
			# Find all table rows
			rows = table.find_all("tr")
			# Progess bar
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
				print("No table rows found")
		print(u"\033[92m\033[1m\n[\u2713] Done\033[0m\033[0m")
	except ConnectionError as e:
		print("[-] Problem connecting to website...")
		print("[-] Exiting...")
		# Remove students.csv file if  exist
		if os.path.exists("Postgraduate-Ghanaian-Applicants.csv"):
				os.remove("Postgraduate-Ghanaian-Applicants.csv")

	except ConnectTimeout as c:
		print("[-] Connection Timeout...")
		print("[*] Retrying...")	
	# Close students.csv file if exist
	if os.path.exists("Postgraduate-Ghanaian-Applicants.csv"):
		csvFile.close()

def distance_diploma_applicants():

	base_url = "https://apps.knust.edu.gh/admissions/check/Home/Distance?group=35&page="
	# Create students.csv file if not exist
	if not os.path.exists("Distance-Diploma-Applicants.csv"):
		os.mknod("Distance-Diploma-Applicants.csv")
	# Open students.csv file
	csvFile = open("Distance-Diploma-Applicants.csv", "wt+")
	writer = csv.writer(csvFile)
	
	try:	
		print("\033[93m[+] Loading...(Please wait)\033[0m")	
		# Loop between total number of pages (total=328)
		for i in range(1,21,1):
			url = base_url+"{}".format(i)
			# Make request to site (https://www.knust.edu.gh)
			req = requests.get(url)   
			soup = BeautifulSoup(req.text, "html.parser")
			# Find table on page
			table = soup.find("table")
			# Find all table rows
			rows = table.find_all("tr")
			# Progess bar
			sys.stdout.write("#")
			sys.stdout.flush()

			try:
				for row in rows:
					csvRow = []
					for cell in row.find_all(["td", "th"]):
						# Correct UnicodeError
						csvRow.append(cell.get_text().encode("ascii", "ignore"))
						
						if len(csvRow) == 3:
							if csvRow[0].isdigit():
								csvRow.pop(0)
								writer.writerow(csvRow)
												
							else:
								None
						else:
							None
			except Exception as e:
				print("No table rows found")
		print(u"\033[92m\033[1m\n[\u2713] Done\033[0m\033[0m")
	except ConnectionError as e:
		print("[-] Problem connecting to website...")
		print("[-] Exiting...")
		# Remove students.csv file if  exist
		if os.path.exists("Distance-Diploma-Applicants.csv"):
				os.remove("Distance-Diploma-Applicants.csv")

	except ConnectTimeout as c:
		print("[-] Connection Timeout...")
		print("[*] Retrying...")	
	# Close students.csv file if exist
	if os.path.exists("Distance-Diploma-Applicants.csv"):
		csvFile.close()

def distance_undergraduate_applicants():

	base_url = "https://apps.knust.edu.gh/admissions/check/Home/Distance?group=5&page="
	# Create students.csv file if not exist
	if not os.path.exists("Distance-Undergraduate-Applicants.csv"):
		os.mknod("Distance-Undergraduate-Applicants.csv")
	# Open students.csv file
	csvFile = open("Distance-Undergraduate-Applicants.csv", "wt+")
	writer = csv.writer(csvFile)
	
	try:	
		print("\033[93m[+] Loading...(Please wait)\033[0m")	
		# Loop between total number of pages (total=328)
		for i in range(1,45,1):
			url = base_url+"{}".format(i)
			# Make request to site (https://www.knust.edu.gh)
			req = requests.get(url)   
			soup = BeautifulSoup(req.text, "html.parser")
			# Find table on page
			table = soup.find("table")
			# Find all table rows
			rows = table.find_all("tr")
			# Progess bar
			sys.stdout.write("#")
			sys.stdout.flush()

			try:
				for row in rows:
					csvRow = []
					for cell in row.find_all(["td", "th"]):
						# Correct UnicodeError
						csvRow.append(cell.get_text().encode("ascii", "ignore"))
						
						if len(csvRow) == 3:
							if csvRow[0].isdigit():
								csvRow.pop(0)
								writer.writerow(csvRow)
												
							else:
								None
						else:
							None
			except Exception as e:
				print("No table rows found")
		print(u"\033[92m\033[1m\n[\u2713] Done\033[0m\033[0m")
	except ConnectionError as e:
		print("[-] Problem connecting to website...")
		print("[-] Exiting...")
		# Remove students.csv file if  exist
		if os.path.exists("Distance-Undergraduate-Applicants.csv"):
				os.remove("Distance-Undergraduate-Applicants.csv")

	except ConnectTimeout as c:
		print("[-] Connection Timeout...")
		print("[*] Retrying...")	
	# Close students.csv file if exist
	if os.path.exists("Distance-Undergraduate-Applicants.csv"):
		csvFile.close()

def distance_postgraduate_applicants():

	base_url = "https://apps.knust.edu.gh/admissions/check/Home/Distance?group=6&page="
	# Create students.csv file if not exist
	if not os.path.exists("Distance-Postgraduate-Applicants.csv"):
		os.mknod("Distance-Postgraduate-Applicants.csv")
	# Open students.csv file
	csvFile = open("Distance-Postgraduate-Applicants.csv", "wt+")
	writer = csv.writer(csvFile)
	
	try:	
		print("\033[93m[+] Loading...(Please wait)\033[0m")	
		# Loop between total number of pages (total=328)
		for i in range(1,70,1):
			url = base_url+"{}".format(i)
			# Make request to site (https://www.knust.edu.gh)
			req = requests.get(url)   
			soup = BeautifulSoup(req.text, "html.parser")
			# Find table on page
			table = soup.find("table")
			# Find all table rows
			rows = table.find_all("tr")
			# Progess bar
			sys.stdout.write("#")
			sys.stdout.flush()

			try:
				for row in rows:
					csvRow = []
					for cell in row.find_all(["td", "th"]):
						# Correct UnicodeError
						csvRow.append(cell.get_text().encode("ascii", "ignore"))
						
						if len(csvRow) == 3:
							if csvRow[0].isdigit():
								csvRow.pop(0)
								writer.writerow(csvRow)
												
							else:
								None
						else:
							None
			except Exception as e:
				print("No table rows found")
		print(u"\033[92m\033[1m\n[\u2713] Done\033[0m\033[0m")
	except ConnectionError as e:
		print("[-] Problem connecting to website...")
		print("[-] Exiting...")
		# Remove students.csv file if  exist
		if os.path.exists("Distance-Postgraduate-Applicants.csv"):
				os.remove("Distance-Postgraduate-Applicants.csv")

	except ConnectTimeout as c:
		print("[-] Connection Timeout...")
		print("[*] Retrying...")	
	# Close students.csv file if exist
	if os.path.exists("Distance-Postgraduate-Applicants.csv"):
		csvFile.close()

# def main():
# 	mainchoice()

# 	choice = int(input(">> "))
# 	if choice == 1:
# 		undergraduate()

# 		choice = int(input(">> "))
# 		if choice == 1:
# 			undergraduate_international_applicants()
# 		elif choice == 2:
# 			undergraduate_ssce_wassce_applicants()
# 		elif choice == 3:
# 			undergraduate_fee_paying_ssce_wassce_applicants()
# 		elif choice == 4:
# 			undergraduate_mature_foreign_applicants()
# 		elif choice == 5:
# 			undergraduate_fee_paying_foreign_applicants()
# 		elif choice == 6:
# 			undergraduate_less_endowed_applicants()
# 		elif choice == 7:
# 			undergraduate_nmtc_upgrade_applicants()
# 		else:
# 			print("Invalid entry")

# 	elif choice == 2:
# 		postgraduate()

# 		choice = int(input(">> "))
# 		if choice == 1:
# 			postgraduate_international_applicants()
# 		elif choice == 2:
# 			postgraduate_ghanaian_applicants()
# 		else:
# 			print("Invalid entry")

# 	elif choice == 3:
# 		distancelearning()

# 		choice = int(input(">> "))
# 		if choice == 1:
# 			distance_diploma_applicants()
# 		elif choice == 2:
# 			distance_undergraduate_applicants()
# 		elif choice == 3:
# 			distance_postgraduate_applicants()
# 		else:
# 			print("Invalid entry")
# 	else:
# 		print("Invalid entry")


if __name__ == '__main__':
	# clear()
	# banner()
	# undergraduate_international_applicants()
	# undergraduate_ssce_wassce_applicants()
	# undergraduate_fee_paying_ssce_wassce_applicants()
	# undergraduate_mature_foreign_applicants()
	# undergraduate_fee_paying_foreign_applicants()
	# undergraduate_less_endowed_applicants()
	# undergraduate_nmtc_upgrade_applicants()
	# postgraduate_international_applicants()
	# postgraduate_ghanaian_applicants()
	# distance_diploma_applicants()
	# distance_undergraduate_applicants()
	# distance_postgraduate_applicants()
	main()
