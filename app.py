from flask import Flask, render_template, request, redirect, url_for, send_from_directory
#googledrivedownloader==0.4
#from google_drive_downloader import GoogleDriveDownloader as gdd

from UGATIT import UGATIT


import os

app = Flask(__name__)


import cv2
import rstr

from utils import *

SAVE_DIR = "./static/images/download"
gan=UGATIT()
gan.build_model() 



@app.route('/', methods = ['GET', 'POST'])
def hokusai():
   
    
   if request.method == 'POST':
      stream = request.files['file'].stream
      img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
      img = cv2.imdecode(img_array, 1)
      rename_str = rstr.xeger(r'^[0-9]{2}[0-9a-zA-Z0-9]{10}') + '.png'
      save_path = os.path.join(SAVE_DIR,rename_str)
      height, width, channels = img.shape[:3]
      cv2.imwrite(save_path, img)
      
      #tt=torch.as_tensor(img)
      #print(type(tt))
      #cv2.imwrite(os.path.join('Base_%d.png' % (10 + 1)), RGB2BGR(tensor2numpy(denorm(tt))) * 255.0)
      gan.test(rename_str,height,width)
      
      
      f = request.files['file']
      #f.save(secure_filename(f.filename))
      return render_template("hokusai.html", user_image = f.filename,chenge_image="/static/images/upload/" + rename_str)

   return render_template('hokusai.html')


if __name__ == '__main__':
   
   app.run(debug=True)