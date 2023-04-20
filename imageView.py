# Imagens binárias 0 e 1
# Imagens em escalas de cinza 0 até 255
# Imagens coloridas rgb

#  OpenCV Open Source Computer Vision desenvolvida pela Intel em 1999

import cv2
# lendo a imagem
img = cv2.imread("butterfly.jpg")

# exibindo a imagem
cv2.imshow("Borboleta", img)

# tempo de exibição
# 0 = infinito
# 1000 = 1 seg
cv2.waitKey(1000)


# uma array  que inicia com 3 colchetes é uma array 3D
print(img)

# logica da array colorida: [[B],[G],[R]]
# imagemColorida=[[array azul],[array verde],[array vermelha]]

# arr_3D = [[[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]]]

arr_3D = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
          [[4, 5, 6], [1, 2, 3], [1, 2, 3]],
          [[7, 8, 9], [1, 2, 3], [1, 2, 3]]]

# print(arr_3D[0][0][0])

# converter uma imagem colorida para cinza

grayImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow("Escalas de cinza", grayImg)

cv2.waitKey(0)

print(grayImg)
