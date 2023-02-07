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
#now = datetime.today()
#print ("Current date ")
#date1=now.strftime("%d%m%Y")
#date2=now.strftime("%d%m0000")
#print(date1)
#print(date2)
print("Enter date in ddmmyyyy format")
date1=input()
print("Enter date in ddmm0000 format")
date2=input()
print(date1)
print(date2)
def getFile(ftp, filename):                                                                   #DEFINITION FOR DOWNLOADING FUNCTION
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except:
        print("Error")

if not os.path.isdir("/home/akshay/Downloads/From_api_ftp/Manual/"+date1+"_FO"):
 os.mkdir("/home/akshay/Downloads/From_api_ftp/Manual/"+date1+"_CM")

print("##########  logging in  ##########")
baseurl='https://www.connect2nse.com/extranet-api/login/1.0'  #live environment
url = 'https://www.connect2nse.com/extranet-api/login/1.0'
myobj = {
"memberCode":"<member code>",
"loginId":"<login id>",
"password":"<Encypted Password>"
}
x = requests.post(url, json = myobj)
print (x)
print(type(x))
j=x.json()
print(j["token"])
TOKEN=j["token"]


print("#########  You are now in Downloading content   ##########") 


url ="https://www.connect2nse.com/extranet-api/common/file/download/1.0?segment=CM&folderPath=varrate&filename=C_VAR1_"+date1+"_6.DAT"
#url ='https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=CM&folderPath=&date=18-01-2023'
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
    with open("/home/akshay/Downloads/From_api_ftp/Manual/"+date1+"_CM/C_VAR1_"+date1+"_6.DAT", 'wb') as f:
     #line = [data.encode('utf8')]
     f.write(data)
else:
    # If the request is unsuccessful, print the status code and the error message
    print(f'Request failed with status code {response.status_code}: {response.text}')



# Set the API endpoint URL
#url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=CM&folderPath=/Downloads&filename=text.txt
url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=CM&folderPath=Reports&filename=<filename>"
#url ='https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=CM&folderPath=&date=18-01-2023'
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
    with open("/home/akshay/Downloads/From_api_ftp/Manual/"+date1+"_CM/<filename>", 'wb') as f:
     #line = [data.encode('utf8')]
     f.write(data)
else:
    # If the request is unsuccessful, print the status code and the error message
    print(f'Request failed with status code {response.status_code}: {response.text}')
    
url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=CM&folderPath=Reports&filename=<filename>
#url ='https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=CM&folderPath=&date=18-01-2023'
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
    with open("/home/akshay/Downloads/From_api_ftp/Manual/"+date1+"_CM/<filename>, 'wb') as f:
     #line = [data.encode('utf8')]
     f.write(data)
    
else:
    # If the request is unsuccessful, print the status code and the error message
    print(f'Request failed with status code {response.status_code}: {response.text}')

url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=CM&folderPath=Onlinebackup&filename=<filename>
#url ='https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=CM&folderPath=&date=18-01-2023'
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
    with open("/home/akshay/Downloads/From_api_ftp/Manual/"+date1+"_CM/<filename>, 'wb') as f:
     #line = [data.encode('utf8')]
     f.write(data)
else:
    # If the request is unsuccessful, print the status code and the error message
    print(f'Request failed with status code {response.status_code}: {response.text}')

url ="https://www.connect2nse.com/extranet-api/common/file/download/1.0?segment=CM&folderPath=bhavcopy&filename=<filename>
#url ='https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=CM&folderPath=&date=18-01-2023'
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
    with open("/home/akshay/Downloads/From_api_ftp/Manual/"+date1+"_CM/<filename>, 'wb') as f:
     #line = [data.encode('utf8')]
     f.write(data)
else:
    # If the request is unsuccessful, print the status code and the error message
    print(f'Request failed with status code {response.status_code}: {response.text}')

j=print("Enter anything to exit")
print("You have now exited the code")

