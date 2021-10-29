from flask import Flask, render_template, request
import os
import cv2
import rstr
from UGATIT import UGATIT
from utils import *

app = Flask(__name__)

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
      return render_template("hokusai.html", user_image = f.filename,chenge_image="/static/images/upload/" + rename_str,before_image="/static/images/download/" + rename_str)

   return render_template('hokusai.html')

@app.route('/questions', methods = ['GET', 'POST'])
def question():
   
    
   if request.method == 'POST':
      print(request.form['impression'])
      print(request.form.getlist('like'))
         
      return render_template("thankyou.html")

   return render_template('question.html')


if __name__ == '__main__':
   
   app.run(debug=True)