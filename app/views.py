import os,sys
import zipfile
import glob
import math

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
   if((int(time)/60)>23):
      newDay = int(date[6:8]) + 1
      newDate = date[0:6] + str(newDay)
      print "Tomorrow! " + newDate
   hours = math.floor(int(time) / 60) % 24
   minutes = round(int(time)%60)

   timeString = int(str(hours) + str(minutes))

   files = os.list(os.path.join('./app/static/img',date))

   
   firstFile = next(files)
   minimal = abs(timeString - int(firstFile[9-13]))
   minFile = firstFile

   for file in files:
      if(abs(timeString - int(file[9-13])) < minimal):
         minimal = abs(timeString - int(file[9-13]))
         minFile = file

   print "hours: " + str(hours) + " minutes: " + str(minutes)
   print "Minfile = " + minFile
   return jsonify(data='all is well at '+date + " at " +time)