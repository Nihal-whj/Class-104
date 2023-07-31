import cv2
img = cv2.imread("poster.jpg")
rocket = img[120:360,400:500]
#cv2.imshow("rocket pic",rocket)
img[0:240,300:400]=rocket
texttoshow = "I am learning python"
cv2.putText(img,texttoshow,(20,220),fontFace=cv2.FONT_ITALIC,fontScale=1,color=(0,0,255))
cv2.imshow("Output of Poster",img)
cv2.waitKey(10000)
