import os
print("WELCOME TO SIMPLE FILE IMPLEMENTATION")
print("1-MODIFY FILE AND DIRECTORY\n2-PERFORM OPERATIONS ON FILE")
mainop=int(input("ENTER OPTION: "))
ifmainop==1:
print("FOR MODIFYING FILE AND DIRECTORY, ENTER THE OPTION NUMBER")
print(" 1-CREATE NEW DIRECTORY\n 2-CHANGE CURRENT WORKING DIRECTORY\n 3-DELETE DIRECTORY \n 4-LIST OUT FILES AND DIRECTORIES\n 5-GET CURRENT WORKING DIRECTORY\n 6-RENAME FILE\n 7-REMOVE FILE\n")
op=input("DO YOU WANT TO PERFORM ANY OF THE ABOVE OPTIONS?(Y/N) ")
while op=="Y":
print("ENTER OPTION")
ch=int(input())
ifch==1:
dirname=input("ENTER THE DIRECTORY NAME: ")
os.makedirs(dirname)
elifch==2:
NEWdirname=input("ENTER THE DIRECTORY NAME: ")
os.chdir(NEWdirname)
elifch==5:
print("CURRENT WORKING DIRECTORY IS: ")
print(os.getcwd())
elifch==3:
DELdirname=input("ENTER THE DIRECTORY NAME: ")
os.rmdir(DELdirname)
elifch==4:
print(os.listdir())
elifch==6:
oldname=input("ENTER OLD NAME: ")
nname=input("ENTER NEW NAME: ")
os.rename(oldname,nname)
else:
remfile=input("ENTER FILENAME TO BE REMOVED: ")
os.remove(remfile)
op=input("DO YOU WISH TO PERFORM ANOTHER OPERATION?  ")
elifmainop==2:
print("THESE ARE THE OPTIONS FOR PERFORMING OPERATIONS ON FILE")
print(" 1-WRITE IN A FILE\n 2-READ FROM A FILE\n 3-APPEND CONTENT TO A FILE\n")
co=input("DO YOU WANT TO PERFORM ANY OF THE ABOVE OPTIONS?(Y/N) ")
while co=="Y":
option=int(input("ENTER YOUR OPTION TO PERFORM IN A FILE: "))
if option==1:
try:
filename=input("ENTER FILE NAME WITH DIRECTORY: ")
myFile=os.open(filename,os.O_WRONLY)
myStr="Hi This is an OS Project"
myData=myStr.encode("UTF-8")
os.write(myFile,myData)
except Exception as e:
print(str(e))
finally:
os.close(myFile)
elif option==2:
try:
filename=input("ENTER FILE NAME WITH DIRECTORY: ")
myFile=os.open(filename,os.O_RDONLY)
myData=os.read(myFile,105)
myStr=myData.decode("UTF-8")
print(myStr)
except Exception as e:
print(str(e))
finally:
os.close(myFile)
else:
try:
filename=input("ENTER FILE NAME WITH DIRECTORY: ")
myFile = os.open(filename, os.O_WRONLY | os.O_APPEND)
myStr = "Appending function"
myData = myStr.encode("UTF-8")
os.write(myFile, myData)
except Exception as e:
print(str(e))
finally:
os.close(myFile)
co=input("DO YOU WISH TO PERFORM ANOTHER OPERATION?  ")
