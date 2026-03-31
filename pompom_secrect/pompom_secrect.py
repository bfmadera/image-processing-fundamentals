from PIL import Image
import numpy as np

# Abrir imagem
img = Image.open('pompom_segredo.bmp').convert("RGB")
arr = np.array(img)

# Separando canais RGB
R = arr[:, :, 0]
G = arr[:, :, 1]
B = arr[:, :, 2]

# Transformando os canais em texto
texto_r = "".join([chr(i) for i in R.flatten(order='C')])
texto_g = "".join([chr(i) for i in G.flatten(order='F')])
texto_b = "".join([chr(i) for i in B.flatten(order='F')])

# Função para extrair apenas a mensagem
def extrair_texto(texto):
    marcador = "segredo: "
    inicio = texto.find(marcador)
    
    if inicio == -1:
        return "segredo não encontrado =("
    
    inicio += len(marcador)   # pula o "segredo: "
    
    fim = texto.find(";", inicio)
    if fim == -1:
        return "segredo também não encontrado =("
    
    return texto[inicio:fim]

print(extrair_texto(texto_r))
print(extrair_texto(texto_g))
print(extrair_texto(texto_b))