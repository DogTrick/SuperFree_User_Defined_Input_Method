import os
import shutil
dir_path = "../data/image_store"
img_path = "/images/"
deformed_img_path = "/deformed_images/"
for i in range(66):
    shutil.rmtree(dir_path + img_path + str(i))
    shutil.rmtree(dir_path + deformed_img_path + str(i))
    os.mkdir(dir_path + img_path + str(i))
    os.mkdir(dir_path + deformed_img_path + str(i))
