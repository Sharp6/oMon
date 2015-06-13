import os,sys
import zipfile

def orderInDirectories():
	basepath = '../app/static/img'
	for filename in os.listdir(basepath):
		path = os.path.join(basepath, filename)
		if os.path.isdir(path):
			continue
		dateString = filename[0:8]
		timeString = filename[9:13]

		print "Timestring is: " + timeString

		if(int(timeString[0:2]) < 12):
			# Change the date to day before
			if(int(dateString[6:8]) == 1):
				# Convert to previous month
				month = dateString[4:6]
				#31-days months
				if (month == 2) or (month == 4) or (month == 6) or (month == 8) or (month == 9) or (month == 11):
					newDirName = dateString[0:4] + str(int(month)-1) + str(31)
				#30-days months
				if (month == 5) or (month == 7) or (month == 10) or (month == 12):
					newDirName = dateString[0:4] + str(int(month)-1) + str(30)
				#februari
				if (month == 3):
					newDirName = dateString[0:4] + str(int(month)-1) + str(28)
				#januari
				if (month == 1):
					newDirName = str(int(dateString[0:4])-1) + str(12) + str(31)
			else:
				# Normal day
				newDirName = dateString[0:6] + str(int(dateString[6:8]) - 1)
		else:
			newDirName = dateString

		newPath = os.path.join(basepath,newDirName,filename)
		print "New path is: " + newPath
		os.renames(path,newPath)
		
def zip():
   basepath = '../app/static/img'
   zipPath = "../tmp/"
   zipLocation = os.path.join(zipPath, "img.zip")
   zipf = zipfile.ZipFile(zipLocation, 'w')
   files = os.listdir(basepath)
   for file in files:
      zipf.write(os.path.join(basepath, file))
   zipf.close()
   return "zip ok.";

if __name__ == "__main__":
	zip()
