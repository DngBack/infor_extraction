# settings.py
from __future__ import annotations

import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

from mlscraper.html import Page
from mlscraper.samples import Sample
from mlscraper.samples import TrainingSet
from mlscraper.training import train_scraper
# scrapegrapthai packages

sys.path.append(str(Path(__file__).parent.parent))  # noqa

dotenv_path = '.env'
load_dotenv(dotenv_path)

OPENAI_KEY = os.environ.get('OPENAI_APIKEY')

# fetch the page to train
einstein_url = 'http://quotes.toscrape.com/author/Albert-Einstein/'
resp = requests.get(einstein_url)
assert resp.status_code == 200

# create a sample for Albert Einstein
# please add at least two samples in practice to get meaningful rules!
training_set = TrainingSet()
page = Page(resp.content)
sample = Sample(page, {'name': 'Albert Einstein', 'born': 'March 14, 1879'})
training_set.add_sample(sample)

# train the scraper with the created training set
scraper = train_scraper(training_set)

# scrape another page
resp = requests.get('http://quotes.toscrape.com/author/J-K-Rowling')
result = scraper.get(Page(resp.content))
print(result)
