
import qrcode

qrCode = qrcode.make('https://www.youtube.com/channel/UCFIfHe1vt7fJUtZbeJLC_CA')

qrCode.save('QRCode_1.png')

print(" Finish ... ")
