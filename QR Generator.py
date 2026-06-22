import qrcode
import os
from PIL import Image

data = input("QR: ")

qr = qrcode.QRCode(version=2, box_size=10, border=5)

qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill='black', back_color='white')

image.save(f'{os.getcwd()}/newqr.png')
img = Image.open(f'{os.getcwd()}/newqr.png')
img.show()
