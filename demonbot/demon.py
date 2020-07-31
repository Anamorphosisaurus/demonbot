import cv2
import numpy as np
import pyautogui
import os, os.path
import glob
import matplotlib.pyplot as plt
import pytesseract
import sys
import time
import random
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
loopcount = 0
loopvar = 1

while loopvar < 5:
    print("start")
    print(loopcount)
    loopcount = loopcount +1
    myScreenshot = pyautogui.screenshot(region=(552,192, 550, 550))
    myScreenshot.save(r'C:\Program Files\demonbot\input\1.jpg')
    img = cv2.imread(r'C:\Program Files\demonbot\input\1.jpg')

    Fsize = 50
    [x,y,z] = (img.shape)
    X = x - 50
    Y = y - 50
    Z = 0;
    count = 0;
    frame = 0;
    frame2 = 0
    xClick = 522+25
    yClick = 192+25
   

    for j in range(0,Y,25):
        xClick = 522+25
        yClick = yClick + 25
        for i in range(0,Y,25):
            M = (img[j:j+50,i:i+50,(0,1,2)])
            occurrences = np.count_nonzero(M == [26,35,92])
            occurrences2 = np.count_nonzero(M == [4,24,71])
            #print(occurrences)
            xClick = xClick + 25
            if (occurrences > 100 and occurrences2 > 100):
                path = 'C:/Program Files/demonbot/demon/'
                frame2 = frame2 + 1
                num2 = str(frame2)
                finalPath = path+num2+'.jpg'
                cv2.imwrite(finalPath, M)
                ranNumx = random.randint(-5,5)
                ranNumy = random.randint(-5,5)
                xClick = xClick + ranNumx
                yClick = yClick + ranNumy
                pyautogui.moveTo(xClick, yClick, duration=0.25)

                action = pyautogui.screenshot(region=(556,162, 46, 20))
                action.save(r'C:\Program Files\demonbot\action\1.jpg')
                actionImg = cv2.imread(r'C:\Program Files\demonbot\action\1.jpg')
                actionText = pytesseract.image_to_string(actionImg)
                print(actionText)
                if(actionText == "Attack" or actionText == "Glee"):
                    pyautogui.moveTo(xClick, yClick, duration=0.25)
                    pyautogui.click()
                    ranNum = random.randint(10,15)
                    
                    time.sleep(ranNum)
                
            
                
           
          
            
            


                path = 'C:\Program Files\demonbot/crawl/'
                frame = frame + 1
                num = str(frame)
                finalPath = path+num+'.jpg'
                cv2.imwrite(finalPath, M)
    
    
    
