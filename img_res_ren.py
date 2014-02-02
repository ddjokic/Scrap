#!/usr/bin/env python

import os
from PIL import Image

''' Image manipulation script - takes single image file or folder, read exif data, rename file(s) as "prefix-YYYYMMDD_HRmmss" and scale them down as per given bigger dimension (similar as sips on unix), using ANTIALIAS algorithm. 
Not carefully tested - will not break computer but may break photos. Use it on your own risk.

(C) 2014, D. Djokic
'''

def get_exif (fn, sizef, prefx, ext):
	img = Image.open (fn)
	exif_data = img._getexif ()
	datetime = exif_data[36867]
	hor_size = exif_data[40962]
	ver_size = exif_data[40963]
	date = datetime.split()
	stamp1 = date[0].replace(':', '')
	stamp2 = date[1].replace(':', '')
	stamp = stamp1 + '_' + stamp2
	namf = prefix + '-'+ stamp
	new_namf = namf + ext
	os.rename (fn, new_namf)
	
	if hor_size > ver_size:
		img_scale = sizef/hor_size
	else: 
		img_scale = sizef/ver_size
	new_img_hor = int(round(img_scale*hor_size, 0))
	new_img_ver = int(round(img_scale*ver_size, 0))
	nimg = Image.open (new_namf)
	newf = nimg.resize ((new_img_hor, new_img_ver), Image.ANTIALIAS)
	newf.save (new_namf)
	return 
		
	
filename = raw_input ("Image File or Folder: ")
size = float(raw_input ("Bigger Image Dimension: "))
prefix = raw_input ("Enter common prefix: ")

outfiles = []
imgfiles = []

if os.path.isfile (filename):
    if os.path.splitext(filename)[1].lower() not in ['.jpg', '.jpeg', '.jfif', '.nef', '.png']:
    	print ("Not Image File!")
    else:
		get_exif (filename, size, prefix)
	
else:
	os.chdir(filename)
	files = os.listdir(filename)
	for file in files:
		if os.path.splitext(file)[1].lower() in ['.jpg', '.jpeg', '.jfif', '.nef', '.png']:
	 		imgfiles.append (file)
	 	elif os.path.splitext(file)[1].lower() not in ['.jpg', '.jpeg', '.jfif', '.nef', '.png']:
			#get_exif(file, size, prefix)
			outfiles.append(file)
			
		elif os.path.splitext(file)[1].lower() == NONE:
			outfiles.append(file)
			
		else:
			outfiles.append (file)
			
	count = len(imgfiles)
	print(count)
	for fnm in range(0, count-1):
		extension = os.path.splitext(file)[1].lower()
		get_exif (imgfiles[fnm], size, prefix, extension)
		


