import os
from PyPDF2 import PdfFileReader as reader

#Parsing existing user information
path2='C:\\Users\\Owner\\Desktop\\ADSPayments'
path1='C:\\Users\\Owner\\Desktop\\.ADSSecretPayment'
i = 0
p = 0
list1 = []
list2 = []

#path1 is the secret files
for root, dirs, files in os.walk(path1):
    for file in files:
        if ".pdf" in file and "March" in file:
            print(os.path.join(root,file))
            list1.append(file)
            studentFile = reader(open(os.path.join(root,file),'rb'))
            studentFields = studentFile.getFormTextFields()
            i += float(studentFields['total'][1:])
            p += 1

#path2 is the regular files
for root, dirs, files in os.walk(path2):
    for file in files:
        if ".pdf" in file and "March" in file:
            print(os.path.join(root,file))
            list2.append(file)
            studentFile = reader(open(os.path.join(root,file),'rb'))
            studentFields = studentFile.getFormTextFields()
            i += float(studentFields['total'][1:])
            p += 1
print(i)
print(p)
print(list(set(list1)-set(list2)))
