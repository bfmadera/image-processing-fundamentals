import numpy as np #matrizes
from PIL import Image #abrir imagem
from scipy.ndimage import convolve #filtro sobel

# 1. Carregar imagem em grayscale - leitura da imagem
img = Image.open('hahaha_bw.png').convert('L') #leitura em intensidade pizel, não em RGB
img = np.array(img, dtype=float)

# 2. Filtros de Sobel
wSx = np.array([
    [-1, -2, -1],  #gradiente x
    [ 0,  0,  0],
    [ 1,  2,  1]
])

wSy = np.array([  #gradiente y
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

# 3. Convolução
gx = convolve(img, wSx)
gy = convolve(img, wSy)

# 4. Remover bordas (1 pixel) - pedido feito no exercício
gx = gx[1:-1, 1:-1]  #remove primeira e a última linhas
gy = gy[1:-1, 1:-1] #remove primeira e a última colunas

# 5. Magnitude do gradiente
M = np.sqrt(gx**2 + gy**2)

# 6. Encontrar posição do maior valor
imm, jmm = np.unravel_index(np.argmax(M), M.shape)
imm = int(imm)
jmm = int(jmm)

print(f"{imm}, {jmm}")