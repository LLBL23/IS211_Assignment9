# pip install beautifulsoup4 lxml
import requests
from bs4 import BeautifulSoup
import csv


url = "https://en.wikipedia.org/wiki/List_of_Nobel_Memorial_Prize_laureates_in_Economic_Sciences"
page = requests.get(url, verify=False)  # collect the list from website
soup = BeautifulSoup(page.content,'html.parser')  # create a BeautifulSoup object

table = soup.find(class_='wikitable sortable')  # pull all text from the wikitable sortable div

f = csv.writer(open("economics_laureates.csv", "w"))  # write to CSV file
f.writerow(["Year", "Laureate (birth/death)", "Country", "Rationale", "PhD (or equivalent alma mater", "Institution (most significant tenure at time of receipt)", "Key Contributions (non-exhaustive)"])  # write the column headers as the first line

for laureate_data in table.find_all('tbody'):  # separate the table into rows
    rows = laureate_data.find_all('tr')

    for row in rows:
        try:
            year = row.find_all('td')[0].text
            laureate_birth_death = row.find_all('td')[2].text
            country = row.find_all('td')[3].text
            rationale = row.find_all('td')[4].text
            phD = row.find_all('td')[5].text
            institution = row.find_all('td')[6].text
            key_contributions = row.find_all('td')[7].text
        except IndexError:
            continue
        f.writerow([year, laureate_birth_death, country, rationale, phD, institution, key_contributions])












if __name__ == "__main__":
    pass