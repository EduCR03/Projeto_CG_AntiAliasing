import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2 as cv

s = 20 # Aumenta a resolução para funcionar como Anti Aliasing
thickness = 20 # Espessura da linha

img_aliased = np.zeros((100, 100, 3), np.uint8) # Cria uma matriz de 0 na tela

cv.circle(img_aliased, (50, 32), 16, (255, 0, 0), 1) # Desenha um circulo (coordenadas, raio, cor, espessura)

pts = np.array([[35, 60], [40, 65], [65, 70], [50, 75], [45, 80]], np.int32) # Determina os vértices do polígono

cv.polylines(img_aliased, [pts], True, (0, 255, 0), 1) # Desenha o polígono (array de vértices, Parâmetro se fecha ou não a figura, cor, espessura)

# Mesmo codigo de criação de figuras mas aumentado em 's' vezes

img_anti_aliased = np.zeros((100*s, 100*s, 3), np.uint8) 

cv.circle(img_anti_aliased, (50*s, 32*s), 16*s, (255, 0, 0), thickness)

pts = np.array([[35, 60], [40, 65], [65, 70], [50, 75], [45, 80]], np.int32)*s 

cv.polylines(img_anti_aliased, [pts], True, (0, 255, 0), thickness) 

plt.figure(figsize=(26, 26)) # Tamanho da imagem mostrada 
plt.subplot(2, 2, 1)
plt.imshow(img_aliased)
plt.subplot(2, 2, 2)
plt.imshow(img_anti_aliased)