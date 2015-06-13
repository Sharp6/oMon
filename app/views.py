import os,sys
import zipfile

from flask import render_template
from app import app

@app.route('/all')
def allImg():
   imgs = sorted(os.listdir('./app/static/img'))
   return render_template('all.html', title='O-Mon', images=imgs)

@app.route('/')
def 