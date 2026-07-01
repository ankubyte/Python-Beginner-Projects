import pyqrcode,png

def genQr():
    text=input("Enter url/text: ").strip()
    myqr=pyqrcode.create(text)
    myqr.svg("myqr.svg", scale = 8)
    myqr.png('myqr.png', scale = 6)

genQr() 