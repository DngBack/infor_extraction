from __future__ import annotations

from autoscraper import AutoScraper

url = 'https://stackoverflow.com/questions/2081586/web-scraping-with-python'

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ['What are metaclasses in Python?']

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)
