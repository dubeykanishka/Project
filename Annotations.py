#To fetch the coordnates of the bounding box from an image

import numpy as np
from PIL import Image
import glob
import cv2

def boundingBox(path):
    for filename in glob.glob(path):
        large = cv2.imread(filename, 1)
        small = cv2.cvtColor(large, cv2.COLOR_BGR2GRAY)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, kernel)

        _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
        connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)

        contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        mask = np.zeros(bw.shape, dtype=np.uint8)

        for idx in range(len(contours)):
            x, y, w, h = cv2.boundingRect(contours[idx])
            mask[y:y+h, x:x+w] = 0
            cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
            r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)

            if r > 0.45 and w > 8 and h > 8:
                cv2.rectangle(large, (x, y), (x+w-1, y+h-1), (0, 255, 0), 1)
                roi=large[y:y+h, x:x+w]
        fat = filename[10:-4]
        with open("D:\\masked\\Label\\" + fat + ".txt","w+") as file:
            for idx in range(len(contours)):
                x, y, w, h = cv2.boundingRect(contours[idx])
                mask[y:y+h, x:x+w] = 0
        
                cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
                r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
                im_w = 1618
                im_h = 881
                cx_new = round(x / im_w, 3)
                w_new = round(w / im_w, 3)
                cy_new = round(y / im_h, 3) 
                h_new = round(h / im_h, 3)
                file.write("0 {1} {2} {3} {4}\n".format(idx,cx_new,cy_new,w_new,h_new))
       
       
      
path1 = "D:\\masked\\*.png"
boundingBox(path1)















#Reference Link: https://stackoverflow.com/questions/69957402/get-bounding-box-coordinates-xywh-from-quad-coordinates-and-normalize-them
