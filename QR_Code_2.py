
import qrcode

qr_Code = qrcode.QRCode(

    border=10,
    box_size=100,
    version=1

)

qr_Code.add_data('https://www.youtube.com/channel/UCFIfHe1vt7fJUtZbeJLC_CA')
qr_Code.make(fit=True)

qr_Image = qr_Code.make_image(fill_color="red",back_color="black")
qr_Image.save('QRCode_2.png')

print(" Finish ... ")
