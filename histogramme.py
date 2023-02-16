import cv2
import matplotlib.pyplot as plt

# Chargement de l'image
image = cv2.imread('solo-256px.png')

# Conversion en niveaux de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Égaliser l'histogramme de l'image
equalized_img = cv2.equalizeHist(gray_image)

cv2.imwrite('equalize.png',equalized_img)
cv2.imwrite('grayImage.png',gray_image)
# Calculer l'histogramme égalisé de l'image
#equalized_hist = cv2.calcHist([equalized_img],[0],None,[256],[0,256])

# Tracer les histogrammes
#plt.plot(cv2.calcHist([gray_image],[0],None,[256],[0,256]), color='gray')
#plt.plot(equalized_hist, color='blue')
#plt.show()