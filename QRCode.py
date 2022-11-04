from unittest import result
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

datum = '''
This is an example qr code bar made by Kolawole Andrew.
In case you need a bar code,contact Kolawole via 08123095594
'''
def maker_qr(data):
    qr = qrcode.QRCode(version=1,box_size=10,border=5)

    qr.add_data(data)

    qr.make(fit=True)
    img = qr.make_image(fill_color='red',back_color='white')

    img.save('E:/FCCprojects/fineqr.png')


#decoding qrcode.
imgs  = Image.open('E:/FCCprojects/fineqr.png')
def decoder(img):
    result = decode(img)
    print(result)

if __name__ == '__main__':
    #maker_qr(datum)
    decoder(imgs)