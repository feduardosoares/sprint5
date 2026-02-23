from PIL import Image # type: ignore # importando o módulo Image da biblioteca PIL

# carregando uma imagem chamada 'tripleten_logo.jpeg' (caminho local)
im = Image.open('tripleten_logo.jpeg')

# obtendo o tamanho da imagem usando o atributo .size e o imprimindo
print(im.size)

# rodando a imagem 90 graus em sentido anti-horário
rotated = im.rotate(90)

# salvando a imagem rodada
rotated.save('rotated.png')