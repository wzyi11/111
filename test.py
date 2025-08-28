import numpy as np
import cv2
import os
from PIL import Image

facesize=(24, 24)
os.makedirs('dataset', exist_ok=True)
num=0
for image in os.listdir('manyimages'):
    num+=1
    processedpath = 'dataset\person' + str(num)
    os.makedirs(processedpath, exist_ok=True)
    if image.endswith('.jpg'):
        initialpath=os.path.join('manyimages', image)
        img=Image.open(initialpath)
        imgwidth, imgheight = img.size
        fw, fh = facesize
        cols = imgwidth // fw
        rows = imgheight // fh
        count = 0
        for i in range(rows):
            for j in range(cols):
                left = j * fw
                top = i * fh
                right = left + fw
                bottom = top + fh
                face = img.crop((left, top, right, bottom))
                savepath = os.path.join(processedpath, str(count) + '.jpg')
                face.save(savepath)
                count += 1
