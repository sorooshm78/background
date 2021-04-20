import random
import os
import re
import requests
from bs4 import BeautifulSoup

def write_file(filename, number):
	with open(filename, 'w') as file:
		file.write(str(number))

def read_file(filename):
	with open(filename, 'r') as file:
		return file.read().strip()

# Download
print("downloading ...") 
try:
	image_name = read_file('index.txt')

	number = int(image_name)
	number += 1
	write_file('index.txt', number)

	link = 'https://www.bing.com/'
	path_image_file = '/home/soroush/Desktop/work/background/download/%s.jpg' % image_name

	page = requests.get(link)
	soup = BeautifulSoup(page.content, 'html.parser')
	source = soup.find('div', class_='img_cont')

	image_url = link
	image_url += re.findall('.*url\((.*)\)',str(source))[0]

	img_data = requests.get(image_url).content

	with open(path_image_file, 'wb') as handler:
		handler.write(img_data)

	print("download %s.jpg" %image_name)

	# Set background
	command = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri %s" %path_image_file
	os.system(command)
	print("set background")

except:
	image_name = random.randint(1, int(read_file('index.txt')))
	print("Internet not connect")
	command = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/soroush/Desktop/work/background/download/%s.jpg" %image_name
	os.system(command)
	print("set local background")
