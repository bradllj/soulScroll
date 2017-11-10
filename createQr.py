import qrcode
import os

qr = qrcode.QRCode(version=1, box_size=5, border=0, 
error_correction=qrcode.constants.ERROR_CORRECT_L)
#qr.add_data("ashes to ashes and dust to dust")
qr.add_data("Dear master  I claim your promise of reward for givers") 
#I claim your promise to reward those who give to you")

qr.make(fit=True)
x = qr.make_image()

img_file = open("/home/chip/H1Qrcode.jpg", 'wb')
x.save(img_file, 'JPEG')
img_file.close()


