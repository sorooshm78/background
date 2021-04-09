import download
import set

image_name = 'bing'
link = 'https://www.bing.com/'
path_image_file = '/home/soroush/Desktop/work/background/image/%s.jpg' % image_name

print("downloading ...")
download.download_image(link, path_image_file)
print("download %s.jpg" % image_name)

print("set background %s.jpg" % image_name)
set.set_image(path_image_file)
