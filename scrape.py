import requests
from bs4 import BeautifulSoup

year = ""
url = "https://www.sports-reference.com/cbb/postseason/2019-ncaa.html"
games =[]

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="bracket")
#print(results.prettify())

teams = results.find_all("div", class_="")
for team in teams:
    games.append(team)
losers = games[1::2]
#for i in losers:
#    print(i, end='\n'*2)

winners = results.find_all("div", class_="winner")
for i in winners:
    print(i, end='\n'*2)