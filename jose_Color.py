@@ -0,0 +1,66 @@
import numpy as np
import cv2

boundaries = [
	([17, 15, 100], [50, 80, 255]),
	#([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 240, 255]),
	#([103, 86, 65], [145, 133, 128])
]

def detectColorOpenCV(image):
    for (lower, upper) in boundaries:

        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")

        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask = mask)

        cv2.imshow("images", np.hstack([image, output]))
        cv2.waitKey(0)

def circleHoughOpenCV(img):
	
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.medianBlur(img, 5)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
	
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=50, param2=30, minRadius=0, maxRadius=40 )

    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow('detected circles', cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def parseImage(img):
	imageA = [[NONE,NONE,NONE,NONE,NONE,NONE],[NONE,NONE,NONE,NONE,NONE,NONE],[NONE,NONE,NONE,NONE,NONE,NONE],[NONE,NONE,NONE,NONE,NONE,NONE],[NONE,NONE,NONE,NONE,NONE,NONE],[NONE,NONE,NONE,NONE,NONE,NONE],[NONE,NONE,NONE,NONE,NONE,NONE]]
	xDem = 0
	yDem = 0	
	for i < 7:
		for j < 6:
			yDem = (480/6)*i
			xDem = (640/7)*j
			tempImg = imageA[i][j]
			j += 1
		i += 1
	return imageA

def main():

    #image = cv2.imread("connect4.jpg")
    cap = cv2.VideoCapture(0)
    ret, image = cap.read()

    #cams_test = 10
    #for i in range(0, cams_test):
    #    cap = cv2.VideoCapture(i)
    #    test, frame = cap.read()
    #    print("i : " + str(i) + " /// result: " + str(test))

    while(cap.isOpened()):
        if ret:
            res = image.shape
            print(res[0]/6)
            print(res[1]/7)

            detectColorOpenCV(image)
            circleHoughOpenCV(image)
			parseImage(image)
        break
main()