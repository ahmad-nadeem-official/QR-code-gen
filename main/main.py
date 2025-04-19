import qrcode

qr = qrcode.QRCode(
    version=1,  # size: 1 to 40 (bigger = more data)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level
    box_size=10,
    border=4,
)

qr.add_data("https://ahmadnadeem.netlify.app")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("ahmad.png")
img.show()
