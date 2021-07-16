from flask import Flask, render_template, request, redirect, url_for, send_from_directory
#from werkzeug import secure_filename

from UGATIT import UGATIT
from utils import *

import torch
import numpy as np
import cv2
#from image_process import canny
from datetime import datetime
import os
import string
import random


SAVE_DIR = "./images"



app = Flask(__name__)

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
      save_path = os.path.join(SAVE_DIR,"aa.jpg")
      cv2.imwrite(save_path, img)
      #tt=torch.as_tensor(img)
      #print(type(tt))
      #cv2.imwrite(os.path.join('Base_%d.png' % (10 + 1)), RGB2BGR(tensor2numpy(denorm(tt))) * 255.0)
      gan.test()
      
      
      f = request.files['file']
      #f.save(secure_filename(f.filename))
      return render_template("hackathon.html", user_image = f.filename)
		
if __name__ == '__main__':
    
      

   app.run(debug = True)