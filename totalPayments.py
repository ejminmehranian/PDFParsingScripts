import os
from PyPDF2 import PdfFileReader as reader

#Parsing existing user information
path = '/Users/Ejmin/Desktop/Mar0918'

i = 0
p = 0
for root, dirs, files in os.walk(path):
	for file in files:
		if ".pdf" in file and "February" in file:
			print(os.path.join(root,file))
			studentFile = reader(open(os.path.join(root,file),'rb'))
			studentFields = studentFile.getFormTextFields()
			i += float(studentFields['total'][1:])
			p += 1
print(i)
print(p)
