#START

import ftplib                                                                               #IMPORTING LIBRARIES
import sys
import os
import gzip
import shutil
from datetime import date

os.chdir("/home/akshay/Downloads/Download_shilpi")                                            #CHANGING PRESENT WORKING DIRECTORY

def getFile(ftp, filename):                                                                   #DEFINITION FOR DOWNLOADING FUNCTION
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except:
        print("Error")


ftp = ftplib.FTP("ftp.connect2nse.com")                                                        #CONNECTING TO FTP
ftp.login("<id>", "<pass>")

ftp.cwd('<path>')                                                                      #CHANGING LOCATION IN FTP 
print("Date for files in format ddmmyy:")
dt=input()                                                                                     #INPUTTING DATE
getFile(ftp,'<name>'+dt+'.lis.gz')
getFile(ftp,'<name>'+dt+'.csv')
ftp.cwd('<path>')
getFile(ftp,dt+'<name>')                                                                #DOWNLOADING FILE

ftp.quit()

ftp = ftplib.FTP("ftp.connect2nse.com")
ftp.login("<id>", "<pass>")

ftp.cwd('/common/VARRate')
getFile(ftp,'C_VAR1_'+dt+'_6.dat')

print("Date for VARRATE file in format ddmmyyyy where yyyy=0000:")
dt2=input()
ftp.cwd('/common/Bhavcopy')
getFile(ftp,dt2+'.md')

ftp.quit()

with gzip.open('<name>'+dt+'.lis.gz', 'rb') as f_in:                                      #UNZIPPING ZIPPED FILE
    with open('<name>'+dt+'.lis', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

with gzip.open(dt+'<name>', 'rb') as f_in:
    with open(dt+'<name>', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

os.remove('C_MG13_90185_'+dt+'.lis.gz')                                                          #REMOVING ZIPPED FILES AFTER EXTRACTION
os.remove(dt+'<name>')                
        
os.mkdir(dt)                                                                                     #MAKING FOLDER

f1='<name>'+dt+'.lis'                                                                     #CREATING VARIABLES TO STORE PATH VALUE
f2='<name>'+dt+'.csv'
f3=dt+'<name>'
f4='C_VAR1_'+dt+'_6.dat'
f5=dt2+'.md'

src_path = r'/home/akshay/Downloads/Download_shilpi/'+f1                                          #MOVING FILES FROM SOURCE PATH TO DESTINATION PATH 
dst_path = r'/home/akshay/Downloads/Download_shilpi/'+dt+'/'+f1
shutil.move(src_path, dst_path)

src_path = r'/home/akshay/Downloads/Download_shilpi/'+f2
dst_path = r'/home/akshay/Downloads/Download_shilpi/'+dt+'/'+f2
shutil.move(src_path, dst_path)

src_path = r'/home/akshay/Downloads/Download_shilpi/'+f3
dst_path = r'/home/akshay/Downloads/Download_shilpi/'+dt+'/'+f3
shutil.move(src_path, dst_path)

src_path = r'/home/akshay/Downloads/Download_shilpi/'+f4
dst_path = r'/home/akshay/Downloads/Download_shilpi/'+dt+'/'+f4
shutil.move(src_path, dst_path)

src_path = r'/home/akshay/Downloads/Download_shilpi/'+f5
dst_path = r'/home/akshay/Downloads/Download_shilpi/'+dt+'/'+f5
shutil.move(src_path, dst_path)

#END
