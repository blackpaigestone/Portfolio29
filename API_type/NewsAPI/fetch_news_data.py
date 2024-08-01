import os
import requests
import pandas as pd
import pyarrow.feather as feather
from dotenv import load_dotenv
from itertools import product
from datetime import datetime

env_path = '/Users/paigeblackstone/Desktop/Portfolio29/Portfolio29/env/newsapi.env'
load_dotenv(env_path)

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

BASE_URL = 'https://newsapi.org/v2/'

countries = ['us', 'de', 'au', 'ca', 'jp', 'cn']
categories = ['business', 'entertainment', 'general', 'technology']
keywords = ['AI', 'technology', 'health', 'economy', 'business','philosophy', 'culture']

def get_custom_headlines(country, category, keyword):
    url = f"{BASE_URL}top-headlines"
    params = {
        'country': country,
        'category': category,
        'q': keyword,
        'pageSize': 10,
        'apiKey': NEWS_API_KEY
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return {}

all_articles = []

for country, category, keyword in product(countries, categories, keywords):
    print(f"Fetching data for country={country}, category={category}, keyword={keyword}")
    data = get_custom_headlines(country, category, keyword)
    articles = data.get('articles', [])
    for article in articles:
        article['country'] = country
        article['category'] = category
        article['keyword'] = keyword
    all_articles.extend(articles)

df = pd.DataFrame(all_articles)


timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'/Users/paigeblackstone/Library/Mobile Documents/com~apple~CloudDocs/news_api_data/newsdata_{timestamp}.feather'

feather.write_feather(df, filename)