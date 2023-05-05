#KHADRAOUI Mohamed El Bachir (CHPS Master 2)

import cv2
import numpy as np


def addtwoimages(img1path, img2path):

    img = cv2.imread(img1path)
    img2 = cv2.imread(img2path)

    result = cv2.add(img, img2)

    cv2.imwrite('base_with_mask.png', result)