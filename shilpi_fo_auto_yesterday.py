import requests
import json
import pandas as pd
import datetime
from datetime import datetime
from datetime import date, timedelta
import pprint
import os
import sys
import time
import glob
import subprocess
import smtplib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from django.utils.encoding import force_bytes, force_str
from urllib import request
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from django.utils.encoding import force_bytes, force_str
import re

os.chdir("/home/akshay/Downloads/From_api_ftp")                                            #CHANGING PRESENT WORKING DIRECTORY
now = datetime.today()
yesterday = now - timedelta(days = 1)

date1=yesterday.strftime("%d%m%Y")
date2=yesterday.strftime("%d%m0000")
#date1='31012023'
#date2='31010000'
print ("Yesterday date ")
print(date1)
print(date2)
if not os.path.isdir("/home/akshay/Downloads/From_api_ftp/"+date1+"_FO"):
 os.mkdir("/home/akshay/Downloads/From_api_ftp/"+date1+"_FO")
def getFile(ftp, filename):                                                                   #DEFINITION FOR DOWNLOADING FUNCTION
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except:
        print("Error")

print("##########  logging in  ##########")
baseurl='https://www.connect2nse.com/extranet-api/login/1.0'
url = 'https://www.connect2nse.com/extranet-api/login/1.0'
myobj = {
"memberCode":"<member code>",
"loginId":"<login id>",
"password":"<encrypted password>"
}
x = requests.post(url, json = myobj)
print (x)
print(type(x))
j=x.json()
print(j["token"])
TOKEN=j["token"]


print("#########  You are now in Downloading content   ##########") 


url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=FO&folderPath=Reports&filename=<filename>"
#url ='https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=FO&folderPath=&date=18-01-2023'
#url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment="+seg+"&folderPath="+path+"&filename="+filename
# Set the headers for the request, including the Authorization header with the token
headers = {'Authorization': 'Bearer ' + TOKEN}
# Make the GET request
response = requests.get(url, headers=headers)
# Check the status code of the response
if response.status_code == 200:
    data=response.content
    r = requests.get(url)
    print(url)
    print(response)
    with open("/home/akshay/Downloads/From_api_ftp/"+date1+"_FO/<filename>", 'wb') as f:
     #line = [data.encode('utf8')]
     f.write(data)
else:
    # If the request is unsuccessful, print the status code and the error message
    print(f'Request failed with status code {response.status_code}: {response.text}')



# Set the API endpoint URL
#url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=FO&folderPath=/Downloads&filename=text.txt
url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=FO&folderPath=Reports&filename=<filename>"
#url ='https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=FO&folderPath=&date=18-01-2023'
headers = {'Authorization': 'Bearer ' + TOKEN}
# Make the GET request
response = requests.get(url, headers=headers)
# Check the status code of the response
if response.status_code == 200:
    
    data=response.content
    #print(data)
    print(url)
    print(response)
    r = requests.get(url)
    with open("/home/akshay/Downloads/From_api_ftp/"+date1+"_FO/<filename>", 'wb') as f:
     #line = [data.encode('utf8')]
     f.write(data)
else:
    # If the request is unsuccessful, print the status code and the error message
    print(f'Request failed with status code {response.status_code}: {response.text}')
    
url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=FO&folderPath=Reports&filename=<filename>"
#url ='https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=FO&folderPath=&date=18-01-2023'
headers = {'Authorization': 'Bearer ' + TOKEN}
# Make the GET request
response = requests.get(url, headers=headers)
# Check the status code of the response
if response.status_code == 200:
    
    data=response.content
    #print(data)
    print(url)
    print(response)
    r = requests.get(url)
    with open("/home/akshay/Downloads/From_api_ftp/"+date1+"_FO/<filename>", 'wb') as f:
     #line = [data.encode('utf8')]
     f.write(data)
    
else:
    # If the request is unsuccessful, print the status code and the error message
    print(f'Request failed with status code {response.status_code}: {response.text}')

url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=FO&folderPath=Onlinebackup&filename=<filename>"
#url ='https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=FO&folderPath=&date=18-01-2023'
headers = {'Authorization': 'Bearer ' + TOKEN}
# Make the GET request
response = requests.get(url, headers=headers)
# Check the status code of the response
if response.status_code == 200:
    
    data=response.content
    #print(data)
    print(url)
    print(response)
    r = requests.get(url)
    with open("/home/akshay/Downloads/From_api_ftp/"+date1+"_FO/<filename>", 'wb') as f:
     #line = [data.encode('utf8')]
     f.write(data)
else:
    # If the request is unsuccessful, print the status code and the error message
    print(f'Request failed with status code {response.status_code}: {response.text}')

url ="https://www.connect2nse.com/extranet-api/common/file/download/1.0?segment=FO&folderPath=&filename=contract.gz"
#url ='https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=FO&folderPath=&date=18-01-2023'
#url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment="+seg+"&folderPath="+path+"&filename="+filename
# Set the headers for the request, including the Authorization header with the token
headers = {'Authorization': 'Bearer ' + TOKEN}
# Make the GET request
response = requests.get(url, headers=headers)
# Check the status code of the response
if response.status_code == 200:
    data=response.content
    r = requests.get(url)
    print(url)
    print(response)
    with open("/home/akshay/Downloads/From_api_ftp/"+date1+"_FO/contract.gz", 'wb') as f:
     #line = [data.encode('utf8')]
     f.write(data)
else:
    # If the request is unsuccessful, print the status code and the error message
    print(f'Request failed with status code {response.status_code}: {response.text}')

url ="https://www.connect2nse.com/extranet-api/common/file/download/1.0?segment=FO&folderPath=MarketReports&filename=<filename>"
#url ='https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=FO&folderPath=&date=18-01-2023'
#url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment="+seg+"&folderPath="+path+"&filename="+filename
# Set the headers for the request, including the Authorization header with the token
headers = {'Authorization': 'Bearer ' + TOKEN}
# Make the GET request
response = requests.get(url, headers=headers)
# Check the status code of the response
if response.status_code == 200:
    data=response.content
    r = requests.get(url)
    print(url)
    print(response)
    with open("/home/akshay/Downloads/From_api_ftp/"+date1+"_FO/<filename>", 'wb') as f:
     #line = [data.encode('utf8')]
     f.write(data)
else:
    # If the request is unsuccessful, print the status code and the error message
    print(f'Request failed with status code {response.status_code}: {response.text}')

'''
print("#########  You are now in Downloading content   ##########")



ftp = ftplib.FTP("ftp.connect2nse.com")                                                        #CONNECTING TO FTP
ftp.login("90185", "Clopen#3")

ftp.cwd('/90185/Reports')                                                                      #CHANGING LOCATION IN FTP 
print("Date for files in format ddmmyy:")
dt=input()             




with gzip.open('C_MG13_90185_'+dt+'.lis.gz', 'rb') as f_in:                                      #UNZIPPING ZIPPED FILE
    with open('C_MG13_90185_'+dt+'.lis', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

with gzip.open(dt+'_90185.txt.gz', 'rb') as f_in:
    with open(dt+'_90185.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

os.remove('C_MG13_90185_'+dt+'.lis.gz')                                                          #REMOVING ZIPPED FILES AFTER EXTRACTION
os.remove(dt+'_90185.txt.gz')                
        
os.mkdir(dt)                                                                                     #MAKING FOLDER

f1='C_MG13_90185_'+dt+'.lis'                                                                     #CREATING VARIABLES TO STORE PATH VALUE
f2='MWST_90185_T_'+dt+'.csv'
f3=dt+'_90185.txt'
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
'''











 
'''
# Set the API endpoint URL
#url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=FO&folderPath=/Downloads&filename=text.txt
url ='https://www.connect2nse.com/extranet-api/common/file/download/1.0?segment=FO&folderPath=ntneat&filename=security.gz'
#url ='https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=FO&folderPath=&date=18-01-2023'
#url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment="+seg+"&folderPath="+path+"&filename="+filename
# Set the headers for the request, including the Authorization header with the token
headers = {'Authorization': 'Bearer ' + TOKEN}
# Make the GET request
response = requests.get(url, headers=headers)
# Check the status code of the response
if response.status_code == 200:
    data=response.content
    #print(data)
    #print(type(data))
    r = requests.get(url)
    with open('/home/akshay/Downloads/From_api_ftp/security.gz', 'wb') as f:
     #line = [data.encode('utf8')]
     f.write(data)
else:
    # If the request is unsuccessful, print the status code and the error message
    print(f'Request failed with status code {response.status_code}: {response.text}')
'''
print("You have now exited the code")

