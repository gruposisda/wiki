#!/usr/bin/python

import ftplib
from datetime import datetime
import os

#take pictures
exec(open('capture_v2.py').read())

#login to server
server = ('143.106.75.73')
ftp = ftplib.FTP(server)
user = 'ftpuser'
password = 'daisa!220'
ftp.login(user,password)
ftp.cwd('/public/pictures/')

#create a dir with the time as name and set as wd
dirName = '{}-{}-{}_{}:{}'.format(now.year,now.month,now.day,
                                  now.hour,now.minute)
ftp.mkd(dirName)
ftp.cwd(dirName)

#read all files from output directory
filesToGo = os.listdir('./out')

for name in filesToGo:
    file = open('./out/'+ name,'rb')
    ftp.storbinary('STOR '+ name,file)
    print('transfering file '+ name)
    file.close()
    print("transfered")

ftp.close()

#remove files from out dir
for file in filesToGo:
    os.remove('./out/'+file)


    

