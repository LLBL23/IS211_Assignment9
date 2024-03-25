import requests
from bs4 import BeautifulSoup
import csv


url = "https://en.wikipedia.org/wiki/List_of_NBA_champions"
page = requests.get(url, verify=False)  # collect the list from website
soup = BeautifulSoup(page.content,'html.parser')  # create a BeautifulSoup object

table = soup.find(class_='wikitable sortable')  # pull all text from the wikitable sortable div

f = csv.writer(open("nba_champs.csv", "w"))  # write to CSV file
f.writerow(["Team", "Win", "Loss", "Apps", "Pct", "Year(s) won", "Year(s) lost"])  # write the column headers as the first line

for champions_data in table.find_all('tbody'):  # separate the table into rows
    rows = champions_data.find_all('tr')
    for row in rows:
        try:
            teams = row.find_all('td')[0].text
            wins = row.find_all('td')[1].text
            losses = row.find_all('td')[2].text
            apps = row.find_all('td')[3].text
            pcts = row.find_all('td')[4].text
            years_won = row.find_all('td')[5].text
            years_lost = row.find_all('td')[6].text
        except IndexError:
            continue
        f.writerow([teams, wins, losses, apps, pcts, years_won, years_lost])




if __name__ == "__main__":
    pass

