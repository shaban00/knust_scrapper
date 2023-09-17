#!/usr/bin/env python3

import csv
from util import *
import os
import sys
import time
import requests
from bs4 import BeautifulSoup


# Base url for website
base_url = "https://apps.knust.edu.gh/admissions/check/Home/"

# List of students path urls
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
    "Distance?group=35&page",
    "Distance?group=5&page",
    "Distance?group=6&page"
]


def students_scrapper(url, end, filename):

    if not os.path.exists(filename):
        os.mknod(filename)

    with open(filename, "wt+") as file:
        writer = csv.writer(file)

        # Heading of the table
        writer.writerow(["Student ID", "Full Name", "Programme"])

        try:
            print("\033[93m[+] Loading...(Please wait)\033[0m")
            for i in range(1, end+1):
                # url of pages
                full_url = url + "{}".format(i)

                req = requests.get(full_url)
                soup = BeautifulSoup(req.text, "html.parser")

                rows = soup.find("table").find_all("tr")
                # rows = table.find_all("tr")
                sys.stdout.write("#")
                sys.stdout.flush()

                try:
                    for row in rows:
                        csv_row = []
                        for cell in row.find_all(["td", "th"]):
                            # Correct UnicodeError
                            cell_text = cell.get_text().encode("ascii", "ignore")
                            csv_row.append(cell_text.decode("utf-8"))

                            if len(csv_row) == 4:
                                if csv_row[0].isdigit():
                                    csv_row.pop(0)

                                    if csv_row[0].isdigit():
                                        writer.writerow(csv_row)

                except Exception:
                    print("No rows found")

                full_url = url

        except ConnectionError:
            print("\033[91m[-]\033[0m Problem connecting to {}".format(base_url)[:-22])

            if os.path.exists(filename):
                os.remove(filename)

        except KeyboardInterrupt:
            print("You pressed Ctrl+C\nExiting...")
            sys.exit(1)

        print("\n\033[92m[*]\033[0m Done...")


def main():

    clear_screen()
    banner()
    mainchoice()

    myLoop = True

    while myLoop:

        choice = int(input("\033[92mchoice>>\033[0m "))

        if choice == 1:
            url = base_url + students_urls[0]
            end = 8
            filename = "undergrad_international_applicants.csv"
            students_scrapper(url, end, filename)
            myLoop = False

        elif choice == 2:
            url = base_url + students_urls[1]
            end = 328
            filename = "undergrad_wassce_applicants.csv"
            students_scrapper(url, end, filename)
            myLoop = False

        elif choice == 3:
            url = base_url + students_urls[2]
            end = 135
            filename = "undergrad_fee_paying_wassce_applicants.csv"
            students_scrapper(url, end, filename)
            myLoop = False

        elif choice == 4:
            url = base_url + students_urls[3]
            end = 2
            filename = "undergrad_mature_applicants.csv"
            students_scrapper(url, end, filename)
            myLoop = False

        elif choice == 5:
            url = base_url + students_urls[4]
            end = 9
            filename = "undergrad_fee_paying_mature_applicants.csv"
            students_scrapper(url, end, filename)
            myLoop = False

        elif choice == 6:
            url = base_url + students_urls[5]
            end = 21
            filename = "undergrad_less_endowed_applicants.csv"
            students_scrapper(url, end, filename)
            myLoop = False

        elif choice == 7:
            url = base_url + students_urls[6]
            end = 4
            filename = "nmtc_applicants.csv"
            students_scrapper(url, end, filename)
            myLoop = False

        elif choice == 8:
            url = base_url + students_urls[7]
            end = 54
            filename = "postgrad_international_applicants.csv"
            students_scrapper(url, end, filename)
            myLoop = False

        elif choice == 9:
            url = base_url + students_urls[8]
            end = 54
            filename = "postgrad_ghanaian_applicants.csv"
            students_scrapper(url, end, filename)
            myLoop = False

        elif choice == 10:
            url = base_url + students_urls[9]
            end = 54
            filename = "distance_learning_diploma_applicants.csv"
            students_scrapper(url, end, filename)
            myLoop = False

        elif choice == 11:
            url = base_url + students_urls[10]
            end = 54
            filename = "distance_learning_undergrad_applicants.csv"
            students_scrapper(url, end, filename)
            myLoop = False

        elif choice == 12:
            url = base_url + students_urls[11]
            end = 54
            filename = "distance_learning_postgrad_applicants.csv"
            students_scrapper(url, end, filename)
            myLoop = False

        elif choice == 99:
            print("\033[92m[*]\033[0m Exiting...")
            time.sleep(1)
            sys.exit(1)

        else:
            clear_screen()
            mainchoice()


if __name__ == '__main__':
    main()
