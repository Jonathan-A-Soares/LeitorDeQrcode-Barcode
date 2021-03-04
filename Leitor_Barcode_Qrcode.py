from pyzbar.pyzbar import decode
from PIL import Image

filename = input("Nome Do Arquivo:")

img = Image.open(filename)
result = decode(img)
for i in result:
    print(i.data.decode("utf-8"))
