import qrcode

qr = qrcode.QRCode(version=None,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=10,
                   border=2)

url="qfsf.link"
qr.add_data(url)
qr.make(fit=True)
img= qr.make_image()
img.save('e:\\ttttttttttttt.png')

