import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from datetime import datetime

dir_paths = [
    "../data/image_store/images", 
    "../data/image_store/deformed_images", 
]
data = np.array([])
for dir_path in dir_paths:
    for i in range(66):
        img_dir = dir_path + "/" + str(i)
        for root, dirs, files in os.walk(img_dir):
            if len(files) != 0:
                for file in files:
                    file_path = img_dir + "/" + file
                    img = cv2.imread(file_path)
                    img = cv2.resize(img, (28, 28))  
                    img = np.mean(img, axis = 2)
                    # img = img / 255
                    img = img.reshape([28, 28, 1])
                    img = img.transpose([1, 0, 2])
                    img = img.reshape(1, 28 * 28)
                    data = np.append(data, i)
                    data = np.append(data, img)

n_col = 1 + 28 * 28
n_row = len(data) // n_col

data = data.reshape(n_row, n_col)
data = pd.DataFrame(data)

now = datetime.now()
datetime = datetime.strftime(now, '%Y_%m_%d %H_%M_%S')
data.to_csv("../data/new_datasets/" + datetime + ".csv", header = False, index = False)