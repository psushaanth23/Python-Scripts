'''
Program to convert any image to jpg
Author : Sushaanth P

Usage :
    - Put this python file in a new folder
    - Copy all the images you want to convert to jpg in this folder
    - Run the script

'''
from PIL import Image
import os

formats = ['.gif','.psd','.webp','.bmp','.eps','.icns','.ico','.im','.jpg','.msp','.pcx','.png','.ppm','.sgi','.tiff','.spi','.xbm','.cur','.dcx','.dds','.fli','.fpx','.gbr','.imt','.mic','.mpo','.pcd','.tga','.wal','.xpm','.wmf','.icns']
Allfiles = []

for format in formats:
	filenames = [entry for entry in os.scandir('.') if entry.name.find(format)!=-1]
	if filenames!=[]:
		Allfiles.append(filenames)
print(Allfiles)

for files in Allfiles:
	for file in files:
		im = Image.open(file.name).convert("RGB")
		im.save(file.name[:-4]+".jpg","jpeg") 	#change this line to change it to some other format
	
