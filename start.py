import os
import re
import requests
from bs4 import BeautifulSoup

image_name = 'background'
link = 'https://www.bing.com/'
path_image_file = '/home/soroush/Desktop/work/background/download/%s.jpg' % image_name

# Download
print("downloading ...") 
try:
	page = requests.get(link)
	soup = BeautifulSoup(page.content, 'html.parser')
	source = soup.find('div', class_='img_cont')

	image_url = link
	image_url += re.findall('.*url\((.*)\)',str(source))[0]

	img_data = requests.get(image_url).content

	with open(path_image_file, 'wb') as handler:
		handler.write(img_data)
		command = "cp ./download/%s.jpg ./local" %image_name
		os.system(command)
	
	print("download %s.jpg" %image_name)
	
	# Set background
	command = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri %s" %path_image_file
	os.system(command)
	print("set background")

except:
	print("Internet not connect")
	command = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/soroush/Desktop/work/background/local/%s.jpg" %image_name
	os.system(command)
	print("set local background")
