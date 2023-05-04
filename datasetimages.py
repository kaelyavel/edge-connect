#KHADRAOUI Mohamed El Bachir (CHPS Master2)

import cv2
import numpy as np
import glob
from maskgeneration import generate_mask_data



def generate_images_and_masks(): #Generates masks from images
    for f in glob.glob('./vanilla_dataset/LEHIGH-ENGINEERING/*/*'):
        ##compression
        img = cv2.imread(f)
        dst = cv2.resize(img, (0,0), fx=0.1, fy=0.1) 
        

        sub = f.replace('.tif', '.png')
        sub = sub.replace('./vanilla_dataset/LEHIGH-ENGINEERING/', '')
        sub = sub.split('/')
        print(sub)
        name = './datasets/images/'+ sub[1]
        mask_name = './datasets/masks/'+ sub[1]
        print(name)

        mask = generate_mask_data(dst)
        
        cv2.imwrite(name, dst)
        cv2.imwrite(mask_name, mask)


def get_outline(): #Generates outline with Sobel Filter
    for f in glob.glob('./datasets/images/*/*'):
        img = cv2.imread(f)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Using the Canny filter to get contours
        edges = cv2.Canny(gray, 20, 30)
        # Using the Canny filter with different parameters
        edges_high_thresh = cv2.Canny(gray, 60, 120)
    
        img = (255-edges_high_thresh)

        sub = f.replace('./datasets/images/', '')
        sub = sub.split('/')
        print(sub)
        name = './datasets/edges/'+ sub[0] +'/'+ sub[1]
        #mask_name = './datasets/masks/'+ sub[1]
        #print(name)
        
        cv2.imwrite(name, img)

get_outline()