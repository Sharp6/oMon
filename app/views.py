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
   dirList = next(os.walk('./app/static/img'))[1]
   return render_template('clock.html', dirList=dirList)


@app.route('/api/getImgBasedOnTime/<date>/<time>')
def getImgBasedOnTime(date=None,time=None):
   if((time/60)>1):
      print "Tomorrow!"
   hours = math.floor(time / 60) % 24
   minutes = round(time%60)
   print "hours: " + hours + " minutes: " + minutes
   return jsonify(data='all is well at '+date + " at " +time)