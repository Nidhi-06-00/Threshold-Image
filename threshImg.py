import cv2
#dst=cv2.threshold(src,threshold,maxValueForThreshold,binary,type)[1]
img = cv2.imread("sample1.jpg")
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresImg = cv2.threshold(grayImg,180,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("thresholdImage2.jpg",thresImg)
