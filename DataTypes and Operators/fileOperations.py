# File Operations

import base64

# Using a list to read line by line 
with open('random.txt','r+') as fl:		# Read & Write both with 'r+'
	contentList = fl.readlines()
	beLine = base64.b64encode(str(contentList[3])) 		# base64 encodes the 4th item in list
	if (contentList[-1] != beLine):		# Check if last line not encoded
	 fl.write("\n"+beLine)				# If not encoded then encode it and write to the file

# Another method -- Simply Read as Strings (for Small Files)
with open('random.txt', 'r') as fl:   
	content = fl.read()  

#Decoding the last line which was encoded by us
print content + " when decoded gives :: " + base64.b64decode(str(contentList[-1]))



