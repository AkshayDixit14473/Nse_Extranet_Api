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
                                                                     #CHANGING LOCATION IN FTP 
print("Date for files in format ddmmyy:")
dt=input()                                                                                     #INPUTTING DATE

ftp.cwd('<path>')
getFile(ftp,dt+'<filename>')                                                                #DOWNLOADING FILE

ftp.quit()

ftp = ftplib.FTP("ftp.connect2nse.com")
ftp.login("<id>", "<pass>")

ftp.cwd('/FaoFtp/FaoCommon/MarketReports')
getFile(ftp,'F_CN01_NSE_'+dt+'.CSV.gz')

ftp.quit()

with gzip.open('F_CN01_NSE_'+dt+'.CSV.gz', 'rb') as f_in:                                      #UNZIPPING ZIPPED FILE
    with open('F_CN01_NSE_'+dt+'.CSV', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

os.remove('F_CN01_NSE_'+dt+'.CSV.gz')                                                          #REMOVING ZIPPED FILES AFTER EXTRACTION             
        
os.mkdir(dt)                                                                                     #MAKING FOLDER
                                                                   #CREATING VARIABLES TO STORE PATH VALUE
f2='F_CN01_NSE_'+dt+'.CSV'
f4='C_VAR1_'+dt+'_6.dat'
f5=dt+'.md'

#src_path = r'/home/akshay/Downloads/Download_shilpi/'+f1                                          #MOVING FILES FROM SOURCE PATH TO DESTINATION PATH 
#dst_path = r'/home/akshay/Downloads/Download_shilpi/'+dt+'/'+f1
#shutil.move(src_path, dst_path)

#src_path = r'/home/akshay/Downloads/Download_shilpi/'+f2
#dst_path = r'/home/akshay/Downloads/Download_shilpi/'+dt+'/'+f2
#shutil.move(src_path, dst_path)

src_path = r'/home/akshay/Downloads/Download_shilpi/'+f2
dst_path = r'/home/akshay/Downloads/Download_shilpi/'+dt+'/'+f2
shutil.move(src_path, dst_path)

#src_path = r'/home/akshay/Downloads/Download_shilpi/'+f4
#dst_path = r'/home/akshay/Downloads/Download_shilpi/'+dt+'/'+f4
#shutil.move(src_path, dst_path)

#src_path = r'/home/akshay/Downloads/Download_shilpi/'+f5
#dst_path = r'/home/akshay/Downloads/Download_shilpi/'+dt+'/'+f5
#shutil.move(src_path, dst_path)

#END
