import os,sys

def orderInDirectories():
	basepath = '../app/static/img'
	for filename in os.listdir(basepath):
		path = os.path.join(basepath, filename)
		if os.path.isdir(path):
			continue
		newDirName = filename[0:8]
		print newDirName

if __name__ == "__main__":
	orderInDirectories()
