import os
from PyPDF2 import PdfFileReader as reader

#Parsing existing user information
path = '/Users/Ejmin/Desktop/FEB182018/ADSRegistrationForms'
i = 0
userId = 1000
for root, dirs, files in os.walk(path):
	for file in files:
		if ".pdf" in file:
			userId+=1
			#print(userId)
			studentFile = reader(open(os.path.join(root,file),'rb'))
			studentFields = studentFile.getFormTextFields()
			print("-----------------------------------")
			print(studentFields["studentName"] + " " +  studentFields["studentLastName"])
			print(studentFields["phoneNumber"])
			print(studentFields["email"])
			#print(studentFields["emergencyContact"])
			if "parentFullName" in studentFields:
				print("Parent name : " + studentFields["parentFullName"])
			
			print(studentFields["className"])
			#print(studentFields["todaysDate"])	
			#print(studentFields)			
