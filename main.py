import os
import re
import base64
import json

# os.system("pip install -r requirements.txt")

import joblib
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import cv2
import sklearn
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict/", methods = ["GET", "POST"])
def predict():
    def convert_img(imgdata):
        imgstr = json.loads(imgdata)["img"]
        imgstr = re.search(r"base64,(.*)", str(imgdata)).group(1)
        with open("./data/temp_img/output.png", "wb") as output:
            output.write(base64.b64decode(imgstr))
    
    oh_tfr = joblib.load("./predict_model/one_hot_transformer.pkl")
    lb_map = {
        0: "0", 
        1: "1", 
        2: "2", 
        3: "3", 
        4: "4", 
        5: "5", 
        6: "6", 
        7: "7", 
        8: "8", 
        9: "9", 
        10: "A", 
        11: "B", 
        12: "C", 
        13: "D", 
        14: "E", 
        15: "F", 
        16: "G", 
        17: "H", 
        18: "I", 
        19: "J", 
        20: "K", 
        21: "L", 
        22: "M", 
        23: "N", 
        24: "O", 
        25: "P", 
        26: "Q", 
        27: "R", 
        28: "S", 
        29: "T", 
        30: "U", 
        31: "V", 
        32: "W", 
        33: "X", 
        34: "Y", 
        35: "Z", 
        36: "a", 
        37: "b", 
        38: "d", 
        39: "e", 
        40: "f", 
        41: "g", 
        42: "h", 
        43: "n", 
        44: "q", 
        45: "r", 
        46: "t", 
        47: "c", 
        48: "i", 
        49: "j", 
        50: "k", 
        51: "l", 
        52: "m", 
        53: "o", 
        54: "p", 
        55: "s", 
        56: "u", 
        57: "v", 
        58: "w", 
        59: "x", 
        60: "y", 
        61: "z", 
        62: " ", 
        63: ",", 
        64: ".", 
        65: "!", 
    }
    imgdata = request.get_data()
    convert_img(imgdata)
    x = cv2.imread("./data/temp_img/output.png")
    x = cv2.resize(x, (28, 28))
    x = np.mean(x, axis = 2) / 255
    x = x.reshape((1, 28 , 28 , 1))
    model = keras.models.load_model("./predict_model/handwrite_keras_model.h5")
    y = model.predict(x)
    label = oh_tfr.inverse_transform(y).reshape([len(y), ])
    label = pd.Series(label).map(lb_map)[0]  
    return json.dumps({"data": str(label)})

@app.route("/add/")
def add():
    return render_template("craete_data.html")

@app.route("/submit/", methods = ["GET", "POST"])
def submit():
    data = request.get_data()
    data = json.loads(data)
    imgdatas = data[:-1]
    label = data[-1]
    for i, imgdata in enumerate(imgdatas):
        imgname = "./data/image_store/images/" + label + "/output" + str(i) + ".png"
        imgstr = re.search(r"base64,(.*)", str(imgdata)).group(1)
        with open(imgname, "wb") as output:
            output.write(base64.b64decode(imgstr))
    return "received!"

if __name__ == "__main__":
    app.run(debug = True)

