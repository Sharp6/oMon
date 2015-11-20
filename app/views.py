import os,sys
import zipfile
import glob
import math

from flask import render_template
from flask import jsonify
from app import app

# Render routes ####################################################################

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

# API routes ####################################################################
@app.route('/api/getImgBasedOnTime/<date>/<time>')
def getImgBasedOnTime(date=None,time=None):
   date = getDateCorrectedForTimeOverflow(date,time)
   time = getTimeString(time)

   files = os.listdir(os.path.join('./app/static/img',date))

   minimal = 1000
   minFile = files[0]

   for file in files:
      if(abs(time - int(file[9:13])) < minimal):
         minimal = abs(time - int(file[9:13]))
         minFile = file
         print "score " + str(minimal) + " for file " + minFile

   print "hours: " + str(hours) + " minutes: " + str(minutes)
   print "Minfile = " + minFile
   return jsonify(imgSrc=minFile)

# Helper functions ##############################################################
def getDateCorrectedForTimeOverflow(date,time):
   if((int(time)/60)>23):
      newDay = int(date[6:8]) + 1
      date = date[0:6] + str(newDay)

   return date

def getTimeNormalized(time): # Normalized means here: corrected for overflow and fixed number of digits
   hours = int(math.floor(int(time) / 60) % 24) # Correct for time overflow
   minutes = int(round(int(time)%60)) # ???

   if(hours < 10):
      hoursString = str(0) + str(hours)
   else:
      hoursString = str(hours)

   if(minutes < 10):
      minutesString = str(0) + str(minutes)
   else:
      minutesString = str(minutes)

   time = int(hoursString + minutesString)

   return time