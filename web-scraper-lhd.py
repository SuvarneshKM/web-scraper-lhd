import requests
from bs4 import BeautifulSoup

page = requests.get("https://localhackday.mlh.io/local-hack-day-share-challenges")

soup = BeautifulSoup(page.content, 'html.parser')

daily = soup.find(id="Daily")

daily_events = daily.find(class_="collection-list w-dyn-items")

for events in daily_events.find_all(class_="hero-sub-head event"):
	print(events.text)
