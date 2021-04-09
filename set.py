import os

def set_image(file_path):
	command = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri %s" %file_path
	os.system(command)
