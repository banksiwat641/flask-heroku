from fileinput import filename
from flask import Flask, jsonify, request
from flask_restful import Api,Resource
from werkzeug.utils import secure_filename
import cv2 as cv
import glob
from pathlib import Path
import os
import numpy as np

app=Flask(__name__)
#api=Api(app)

#app.config['UPLOAD_FOLDER']="static/images"
@app.route('/')
def hello():
    return "Hello test-Heroku"

ss=''
@app.route('/upload',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST' :
        f=request.files['file'] 
        f.save('uploads/'+secure_filename(f.filename))
        filename=f.filename
        ss=str(filename)
        print('this is '+ss)
        return ss
    if request.method == 'GET' :
        path = "uploads"
        files = os.listdir(path)
        for file in files:
            if file.endswith(('.jpg', '.png', 'jpeg')):
                img_path =  file
                img=cv.imread(str(img_path))
                #cv.imshow('',img)
                imgre=cv.resize(img,(400,500))
                g_img=cv.cvtColor(imgre,cv.COLOR_BGR2GRAY)
                thresh,th=cv.threshold(g_img,100,255,cv.THRESH_BINARY)
                kernel = np.ones((2,2),np.uint8)
                images=cv.dilate(th,kernel,iterations=2)
                sumpix=np.sum(images==255)
                print(sumpix)
                print(str(upload_file))
                #print(str(img_path))
                #cv.waitKey(0)
                #cv.destroyAllWindows()  
                return {"Pixel":str(sumpix)}



if __name__ == "__main__":
    app.run(debug=True)
