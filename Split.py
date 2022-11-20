import cv2
import glob

def split(imgs):
    count = 0
    for filename in glob.glob(imgs):
        img = cv2.imread(filename, 1)  #returns image in numpy
        ## Using 1 to read image in color mode
        for r in range(0,img.shape[0],1000): #rows
            for c in range(0,img.shape[1],1000): #columns
                count +=1
                cv2.imwrite(f"E:\\Kanishka\\Dataset\\Crop_fullData_WCT\\" + str(count) + ".png",img[r:r+1000, c:c+1000,:])

loc = "E:\\Kanishka\\Full_DataWCT\\*.png"
#img = cv2.imread('000217.png')
split(loc)
#Reference: https://stackoverflow.com/a/53756054/19294274
