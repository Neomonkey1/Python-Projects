
import os

# making variable for file path to be used
filePath = 'C:\\Python_projects\\'

print(filePath)

#using listdir() to list the names of all the files in directory
list_dir = os.listdir(filePath)

print(list_dir)


fileName1 = 'test.txt'
fileName2 = 'anotherTest.txt'

#using path.join() to concatenate the files to make absolute path
abPath1 = os.path.join(filePath,fileName1)
abPath2 = os.path.join(filePath,fileName2)

print(abPath1, abPath2)

#using the getmtime() to return the time of last mod
file_time1 = os.path.getmtime(abPath1)
file_time2 = os.path.getmtime(abPath2)

print(file_time1, file_time2)
