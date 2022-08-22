import pyqrcode

from pyqrcode import QRCode

print("Please enter a URL:")
user_url = input()

if user_url.find(".") != -1:
    print("Please enter a filename:")
    file_name = input()

    url = pyqrcode.create(user_url)
    url.png(f"{file_name}.png", scale = 8)

    print("Your QR is generated.")
else:
    print("Please enter a valid URl")

# if user_url contains . then valid URL otherwise invalid URL