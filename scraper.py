from bs4 import BeautifulSoup
import requests
import re
import csv

leagues = [
    'https://www.transfermarkt.us/premier-league/startseite/wettbewerb/GB1',
    'https://www.transfermarkt.us/primera-division/startseite/wettbewerb/ES1',
    'https://www.transfermarkt.us/serie-a/startseite/wettbewerb/IT1',
    'https://www.transfermarkt.us/bundesliga/startseite/wettbewerb/L1',
    'https://www.transfermarkt.us/ligue-1/startseite/wettbewerb/FR1'
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

team_ids = set()
csv_file = 'teams.csv'


def get_teams(league_url, year):
    ext = f'/plus/?saison_id={year}'
    response = requests.get(league_url + ext, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    count = 0

    a_tags = soup.find_all('a', href=re.compile(r'/[^/]+/startseite/verein/\d+'))
    for tag in a_tags:
        href = tag.get('href')
        match = re.search(r'/(?P<name>[^/]+)/startseite/verein/(?P<id>\d+)', href)
        if match:
            name = match.group('name')
            team_id = match.group('id')
            if team_id not in team_ids:
                team_ids.add(team_id)
                writer.writerow([name, team_id])
                count += 1
    print(f'Added {count} teams')

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'id'])

    for year in range(2020, 2024):
        ext = f'/plus/?saison_id={year}'
        for league in leagues:
            match = re.search(r'/([^/]+)/startseite', league)
            if match:
                name = match.group(1)
            print(f'Getting teams for {name} in {year}')
            get_teams(league, year)


