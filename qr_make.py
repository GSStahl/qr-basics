import cv2 as cv
import qrcode
from PIL import Image, ImageDraw
from pyzbar import pyzbar
import sys

try:
	box_size = int(sys.argv[3])
	border = int(sys.argv[4])
	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_H,
		box_size=box_size,
		border=border,
	)
except:
	try:
		box_size = int(sys.argv[4])
		qr = qrcode.QRCode(
			version=1,
			error_correction=qrcode.constants.ERROR_CORRECT_H,
			box_size=box_size,
		)
	except:
		qr = qrcode.QRCode(
			version=1,
			error_correction=qrcode.constants.ERROR_CORRECT_H,
		)

try:
	qr.add_data(sys.argv[1])
except:
	print("Error med indatat (parameter 1)")
try:
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    img.save(sys.argv[2])
except:
	print("Problem med filnamn (parameter 2)", sys.exc_info())
