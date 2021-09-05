# Creator: Jankees Softwares
# Date: 31/07/2021
# Version: 1.0
# About: This tool is used for translate link in qrcode 
# image, this software is distributed free (code free)
# Contact: jankees.software.66@gmail.com

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
