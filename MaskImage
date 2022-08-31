import cv2
import glob

def path(img):
    for filename in glob.glob(img):
        #reads the image
        im = cv2.imread(filename, 1)
        # convert to hsv
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        #set range to detect the purple color objects
        #HSE means Hue, saturation, value
        mask = cv2.inRange(hsv, (134, 81, 180), (138, 112,219))
        f = filename[24:-4]
        #save the image
        cv2.imwrite("D:\\UCC\\Project\\Masked_Full_DataWCT\\" + f + ".png", mask)

loc = "E:\\Kanishka\\Full_DataWCT\\b_002237.png"
path(loc)