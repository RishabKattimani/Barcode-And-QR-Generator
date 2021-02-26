#------------------------------------------------------------------------------
# Simpler Text QR Code
import qrcode

# qr = qrcode.make('Hello World')
# qr.save('MyQR.png')

#------------------------------------------------------------------------------
# Linked QR Code

qr = qrcode.QRCode(
    version = 1,
    box_size = 15,
    border = 15
    )

data = 'https://www.youtube.com/c/RishabTeachesTech/'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill = 'black', back_color = 'white')
img.save('Linked-Code.png')
