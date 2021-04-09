import re
import requests
from bs4 import BeautifulSoup

def download_image(link, image_file):
	page = requests.get(link)
	soup = BeautifulSoup(page.content, 'html.parser')
	source = soup.find('div', class_='img_cont')

	image_url = link
	image_url += re.findall('.*url\((.*)\)',str(source))[0]

	img_data = requests.get(image_url).content
	with open(image_file, 'wb') as handler:
		handler.write(img_data)
