import os,sys

def orderInDirectories():
	basepath = '../app/static/img'
	for filename in os.listdir(basepath):
		path = os.path.join(basepath, filename)
		if os.path.isdir(path):
			continue
		dateString = filename[0:8]
		timeString = filename[9:13]

		print timeString
		

if __name__ == "__main__":
	orderInDirectories()
