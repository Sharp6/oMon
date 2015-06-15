import os,sys
import zipfile
import glob

from flask import render_template
from flask import jsonify
from app import app

@app.route('/all')
def allImg():
   imgs = sorted(os.listdir('./app/static/img'))
   return render_template('all.html', title='O-Mon', images=imgs)

@app.route('/')
def recent():
   newest = max(glob.iglob('./app/static/img/*.jpg'), key=os.path.getctime)
   filename = os.path.split(newest)
   return render_template('index.html', img=filename[1])

@app.route('/clock')
def renderClock():
   print os.walk('./app/static/img')[1]
   return render_template('clock.html')


@app.route('/api/getImgBasedOnTime/<time>')
def getImgBasedOnTime(time=None):
   return jsonify(data='all is well at '+time)