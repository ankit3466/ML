import pytesseract
import cv2
from nltk.corpus import stopwords
import nltk
import matplotlib.pyplot as plt

img = cv2.imread('book.jpg',cv2.IMREAD_COLOR)

config=('-l eng --oem 1 --psm 3')

text=pytesseract.image_to_string(img,config=config)

f=open('news.txt','w+')
f.write(text)
f.close()

removed=[i for i in text.split() if i.lower() not in stopwords.words('english')]

freq_data=nltk.FreqDist(removed)

freq_data.plot(20)
