import os


fileLocation='the location of the file you want to rename'
os.chdir(fileLocation)

#this increments the filenames by 5 ex: newFileName005,newFileName010
x=5
x=str (x)

for filename in os.listdir('.'):
    os.rename(filename, 'newFileName'+x.zfill(3))
    x=str(int(x)+5)
