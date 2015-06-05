import os,sys
import zipfile

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
   imgs = sorted(os.listdir('./app/static/img'))
   return render_template('index.html', title='O-Mon', images=imgs)

@app.route('/zip')
def zip():
   zipf = zipfile.ZipFile('./tmp/img.zip', 'w')
   files = os.listdir('./app/static/img')
   for file in files:
      zipf.write('./app/static/img/' + file)
   zipf.close()
   return "zip ok"
