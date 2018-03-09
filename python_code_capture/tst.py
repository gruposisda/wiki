import ftplib

server = ('143.106.75.73')
ftp = ftplib.FTP(server)
user = 'ftpuser'
password = 'daisa!220'
ftp.login(user,password)
#execfile('../piloto_rafa/preview.py')
import('../piloto_rafa/capture')
