import cv2 as cv
import numpy as np

img = cv.imread("poster.jpg")
text = "Voa foguetao"


# as linhas sao equivalentes a altura  e as colunas a largura
rocket = img[130:300, 410:480]

# precisamos colar a imagem de acordo com a diferença exata que a imagem possui
# x : 130, y: 70

img[0:170, 530:600] = rocket


cv.putText(img, text, (20, 20), fontFace=cv.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1, color=(210, 54, 76))

cv.imshow("cartao", img)
cv.waitKey(0)


# metodo putText(img,text,textposition,textfont,fontscale,color)
