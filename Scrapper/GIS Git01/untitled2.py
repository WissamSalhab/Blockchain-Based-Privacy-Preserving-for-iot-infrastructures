# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 23:48:14 2021

@author: lahza
"""

from serpapi import GoogleSearch
import os

params = {
    "engine": "google",
    "q": "coffee",
    "tbm": "isch",
    "api_key": os.getenv("API_KEY"),
}

client = GoogleSearch(params)
data = client.get_dict()

print(f"Raw HTML: {data['search_metadata']['raw_html_file']}")
print(f"JSON endpoint: {data['search_metadata']['json_endpoint']}")
print()

print("Images results")

for result in data['images_results']:
    print(f"""
Title: {result['title']}
Source: {result['source']}
Link: {result['link']}
Thumbnail: {result['thumbnail']}
""")