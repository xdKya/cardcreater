import cv2
import numpy as np

black = np.zeros([600, 600])

# f_row = black[1:2]
# print("linha f:", f_row)

# f_col = black[:, 1:3]
# print(f_col)

black[200:300, 200:300] = 255
black[400:500, 400:500] = 255
print(black)
cv2.imshow("black", black)
cv2.waitKey(0)

# acessar uma array 2D:
# [linha_inicial : linha_final, coluna_inicial : coluna_final]
