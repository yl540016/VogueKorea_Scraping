from bs4 import BeautifulSoup
import requests
import re

import csv

csv_filename = "vogue_data.csv"

crawling_url = "http://www.vogue.co.kr/category/fashion/page/2"

csv_open = open(csv_filename, 'w+', encoding='utf-8')
csv_writer = csv.writer(csv_open)

csv_writer.writerow( ('title', 'image_url' ) )

response = requests.get(crawling_url)

bs = BeautifulSoup(response.text, 'html.parser')

article_list = bs.find_all("article", { "id": re.compile('post-*')})

for article in article_list:
	h2_title = article.find_all('h2')
	h2_title_text = h2_title[0].text
	print("h2_title_text=", end=""), print(h2_title_text)

	img = article.find('img')
	print("image_url=", end=""), print(img['src'])

	csv_writer.writerow( (h2_title_text, img['src'] ) )

csv_open.close() 
