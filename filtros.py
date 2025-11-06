# Projeto de Visão Computacional - Filtros
import cv2 #Biblioteca principal para visão computacional e processamento de imagens.
import numpy as np #Usado para operações matemáticas e manipulação de matrizes.
import matplotlib.pyplot as plt #Biblioteca para visualização de dados e imagens.
from google.colab import files #Permite enviar arquivos direto do notebook.

uploaded = files.upload()

if uploaded:  # verifica se o arquivo foi enviado
    for nome_arquivo in uploaded.keys():
        imagem = cv2.imread(nome_arquivo, cv2.IMREAD_GRAYSCALE)

    # Aplica o filtro de Sobel para detectar bordas
    sobel_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=3)
    sobel_mag = np.sqrt(sobel_x**2 + sobel_y**2)
    sobel_mag = np.uint8(sobel_mag)

    # Aplica o filtro Laplaciano (segunda derivada) para detectar bordas em todas as direções
    laplaciano = cv2.Laplacian(imagem, cv2.CV_64F, ksize=3)
    laplaciano = np.uint8(np.absolute(laplaciano))
    
    # Aplica o Detector de Bordas de Canny
    canny = cv2.Canny(imagem, 100, 200)

    titulos = ['Original', 'Sobel (Magnitude)', 'Laplaciano', 'Canny']
    imagens = [imagem, sobel_mag, laplaciano, canny]

    plt.figure(figsize=(12,6))
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(imagens[i], cmap='gray')
        plt.title(titulos[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()
else:
    print("No files were uploaded.")
