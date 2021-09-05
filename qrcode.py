

import os

def qrcode():
    while True:
        import pyqrcode
        import png
        from pyqrcode import QRCode

        QRCode = input("Insira o link para gerar o QRCode: ")

        url = pyqrcode.create(QRCC)
        url.png(r"qr.png", scale = 8)

def banner():
    os.system("figlet -f slant QRCode|lolcat")
    qrcode()

banner()
