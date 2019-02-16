# File Operations

import base64

with open('random.txt','r+') as fl:		# Read & Write both with 'r+'
	contentList = fl.readlines()
	beLine = base64.b64encode(str(contentList[3])) 		# base64 encodes the 4th item in list
	if (contentList[-1] != beLine):
	 fl.write("\n"+beLine)

#Without List
with open('random.txt', 'r') as fl:
	content = fl.read()

print content + " when decoded gives :: " + base64.b64decode(str(contentList[-1]))


