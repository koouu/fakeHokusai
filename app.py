from flask import Flask, render_template, request, redirect, url_for, send_from_directory
#from googledrivedownloader import GoogleDriveDownloader as gdd
# from werkzeug import secure_filename

import os

"""
import cv2

from UGATIT import UGATIT
from utils import *

import torch
import numpy as np

#from image_process import canny
from datetime import datetime

import string
import random
import rstr
"""


SAVE_DIR = "./static/images/download"



app = Flask(__name__)
"""
@app.route('/upload')
def upload_file():
   return render_template('hackathon.html')


@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
    
   gan=UGATIT()
   gan.build_model()  
   if request.method == 'POST':
      stream = request.files['file'].stream
      img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
      img = cv2.imdecode(img_array, 1)
      rename_str = rstr.xeger(r'^[0-9]{2}[0-9a-zA-Z0-9]{10}') + '.png'
      save_path = os.path.join(SAVE_DIR,"aa.jpg")
      cv2.imwrite(save_path, img)
      
      #tt=torch.as_tensor(img)
      #print(type(tt))
      #cv2.imwrite(os.path.join('Base_%d.png' % (10 + 1)), RGB2BGR(tensor2numpy(denorm(tt))) * 255.0)
      gan.test(rename_str)
      
      
      f = request.files['file']
      #f.save(secure_filename(f.filename))
      return render_template("hackathon.html", user_image = f.filename,chenge_image="/static/images/upload/" + rename_str)

"""
@app.route("/")
def hello():
   
   if (os.path.exists('./models/HokusaiAI.pt')):
      return "Hello"
   else:
      return "Not Hello"
   
   #return render_template('ch.html')

@app.route('/test')
def test():
   return render_template('hokusai.html')

if __name__ == '__main__':
   """
   gdd.download_file_from_google_drive(file_id='1xmKOuYYdja_awSjV29EiaU5guIi6nLL0',
                                    dest_path='./models/HokusaiAI.pt',
                                    unzip=False)
   
   """

   app.run(debug = True)