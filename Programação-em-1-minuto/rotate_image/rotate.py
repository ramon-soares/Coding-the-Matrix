# pip install Pillow
from PIL import Image

imagem = Image.open("torre_bw.jpg")
imagem = imagem.rotate(90)
imagem.show()