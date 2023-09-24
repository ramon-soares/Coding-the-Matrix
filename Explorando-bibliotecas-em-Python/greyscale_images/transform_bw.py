# pip install Pillow

from PIL import Image

imagem = Image.open("torre.jpg")
imagem_transformada = imagem.convert("L")
imagem_transformada.save("torre_transformada.jpg")
imagem_transformada.show()
