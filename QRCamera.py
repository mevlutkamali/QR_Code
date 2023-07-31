
from pyzbar import pyzbar
from PIL import Image

qr = pyzbar.decode(Image.open('QRCode_2.png'))

print(" QR : " , qr[0].data.decode('ascii'))