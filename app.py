from flask import Flask, render_template, request
import os
import cv2
import rstr
from UGATIT import UGATIT
from utils import *
import csv

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
   type_list=['type',1,2,3,4,5]
   like_list=['like']
   play_list=['play']
   with open('data.csv', 'r') as f:
      
      reader = csv.DictReader(f)
      
      for row in reader:
         cnt=0
         for i in row:
            
            
            if row['type']=='play' and cnt!=0:
               play_list.append(int(row[str(cnt)]))
            if row['type']=='like' and cnt!=0:
               like_list.append(int(row[str(cnt)]))
            cnt=cnt+1
         print(row)
      f.close()
      
   
   if request.method == 'POST':
      if request.form['impression']!='':
         with open('impression.txt', 'a') as f:
            f.write(request.form['impression']+'\n')
            f.close()
      if request.form['next']!='':
         with open('next.txt', 'a') as f:
            f.write(request.form['next']+'\n')
            f.close()

      

         print(request.form['impression'])
      for i in request.form.getlist('play'):
         play_list[int(i)]=play_list[int(i)]+1
      for i in request.form.getlist('like'):
         like_list[int(i)]=like_list[int(i)]+1
      print(request.form.getlist('like'))
      print(like_list)
      with open('data.csv', 'w', newline='') as f:
         writer = csv.writer(f)
         writer.writerow(type_list)
         writer.writerow(play_list)
         writer.writerow(like_list)
      return render_template("thankyou.html")

   return render_template('question.html')


if __name__ == '__main__':
   
   app.run(debug=True)