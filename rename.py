	import os

i=1
directory = os.path.join("c:\\","/home/chandu/Desktop/project: forming collage/paris_attacks/test_data")
for root,dirs,files in os.walk(directory):
	for file in files:
		temp = file
		print "temp: ", temp
		print "img"+str(i)+".jpg"

		path = os.path.join(directory, file)
        	target = os.path.join(directory, "img"+str(i)+".jpg")
	#	if file.endswith(".txt"):
		os.rename(path, target)
		i=i+1
