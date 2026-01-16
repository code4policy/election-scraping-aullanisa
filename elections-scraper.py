# Copy/paste the code from the IMDB scraper ONE LINE AT A TIME
#
# When you paste the line, review what it does and modify it to 
# scrape this elections website instead of IMDB

import requests
url = "https://electionstats.state.ma.us/elections/search/year_from:2025/year_to:2025"

# get the page
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
response = requests.get(url, headers=headers)

# extract HTML as structured "soup"
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# get each row of the table (what is the css selector for the whole row?)
candidates = soup.select('.election_item')

# Loop through the rows and extract the year
for candidate in candidates:
    # get css selector '.year' from inside the winner
    year = candidate.select_one('.year').get_text()
    name = candidate.select_one('.name').get_text()
    # within the election, grab the second element - the office
    office = candidate.select('td')[1].get_text()  
    party = candidate.select_one('.party').get_text()
  
    print(name, party, year, office)
