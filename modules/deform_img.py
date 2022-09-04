import os
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from datetime import datetime

dir_path = "../data/image_store/images"
deformed_dir_path = "../data/image_store/deformed_images"
data = np.array([])
for i in range(66):
    img_dir = dir_path + "/" + str(i)
    for root, dirs, files in os.walk(img_dir):
        if len(files) != 0:
            n = 0
            for file in files:
                file_path = img_dir + "/" + file
                img = cv2.imread(file_path)
                # img = img / 255
                h, w, d = img.shape
                for n_deform in range(4):
                    dw = w * (random.random() - 0.5) / 8
                    dh = h * (random.random() - 0.5) / 8
                    center = ((w + dw) // 2, (h + dh) // 2)
                    angle = random.randint(1, 20)
                    scale = 1 + (random.random() - 0.5) / 3
                    M = cv2.getRotationMatrix2D(center, angle, scale)
                    rotate_img = cv2.warpAffine(img, M, (w, h))
                    # plt.imshow(rotate_img, cmap = "gray")
                    # plt.show()
                    cv2.imwrite(deformed_dir_path + "/" + str(i) + "/output" + str(n) + ".png", rotate_img)
                    n += 1
                    
