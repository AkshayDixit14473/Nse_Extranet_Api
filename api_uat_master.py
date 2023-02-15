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
'''

function downloadDir(location, dest)
    list = filesAtlocation(location)
    for obj in list
        if obj is file
            if exists(dest/obj)
                # do nothing
            else
                download(obj, dest)
            end
        else
            downloadDir(location/obj, dest/obj/)
        end
    end
end

'''
def commonlisting(path, seg):
   print("#########  You are now in listing content  ##########")
   list=[]
   #url1 = 'https://www.devconnect2nse.com/extranet-api/logout/1.0'
   #myobj1 = {
   #"memberCode":"90185",
   #"loginId":"14473"
   #}
   #seg="CM"
   #path="/"
   import requests
   # Replace <TOKEN> with your actual token
   # Set the API endpoint URL
   url = "https://www.devconnect2nse.com/extranet-api/common/content/1.0?segment="+seg+"&folderPath="+path
   # Set the headers for the request, including the Authorization header with the token
   headers = {'Authorization': 'Bearer ' + TOKEN}
   # Make the GET request
   response = requests.get(url, headers=headers)
   # Check the status code of the response
   if response.status_code == 200:
       # If the request is successful, print the response data
       #print(response.json())
       data=response.json()
       print(type(data))
       print(data.keys())
       #print(data["data"].keys())
       print("************************************   RESPONSE   ************************************")
       #print(data)
       #print (data["data"])
       for k in data["data"]:
        #print(type(k))
        #if(k["type"]=='File'):
         print(k["name"])
         list.append(k["name"])
         #print(" is a file\n")
         #obj=k["name"]
         #download(seg, path, obj)
        #else:
         #print(k["name"])
         #path=k["name"]
         #print(" is a folder\n")
         #download_dir(path, dest): 
       #for k in data["data"]:
        #print(type(k))
        #print(k["name"])
       print("**************************************   END   **************************************")
       #data=response.content()
       #print(type(data))
       #json_object = json.loads(data)
       #json_formatted_str = json.dumps(json_object, indent=2)
       #print(json_formatted_str)
       r = requests.get(url)
   else:
       # If the request is unsuccessful, print the status code and the error message
       print(f'Request failed with status code {response.status_code}: {response.text}')


def commonmaster(path, seg):
   print("#########  You are now in master content  ##########") 

   #url1 = 'https://www.devconnect2nse.com/extranet-api/logout/1.0'
   #myobj1 = {
   #"memberCode":"90185",
   #"loginId":"14473"
   #}
   #seg="CM"
   #path="/"
   import requests
   # Replace <TOKEN> with your actual token
   # Set the API endpoint URL
   url = "https://www.devconnect2nse.com/extranet-api/common/content/1.0?segment="+seg+"&folderPath="+path
   # Set the headers for the request, including the Authorization header with the token
   headers = {'Authorization': 'Bearer ' + TOKEN}
   # Make the GET request
   response = requests.get(url, headers=headers)
   # Check the status code of the response
   if response.status_code == 200:
       # If the request is successful, print the response data
       #print(response.json())
       data=response.json()
       print(type(data))
       print(data.keys())
       #print(data["data"].keys())
       print("************************************   RESPONSE   ************************************")
       commonlisting(path, seg)
       if not os.path.isdir("/home/akshay/Downloads/From_api_ftp/"+seg+"_COMMON/"+path):
        os.mkdir("/home/akshay/Downloads/From_api_ftp/CM_COMMON/"+path)
       #print(data)
       #print (data["data"])
       for k in data["data"]:
        #print(type(k))
        print(path)
        
        if(k["type"]=='File'):
         print(k["name"]+" is a file\n")
         obj=k["name"]
         path_to_file = "/home/akshay/Downloads/From_api_ftp/"+seg+"_COMMON/"+path+"/"+obj
         check_file = os.path.isfile(path_to_file)
         if check_file == True:
          print(f'The file {path_to_file} exists')
         else:
          print(f'The file {path_to_file} does not exist')
          commondownload(seg, path, obj)
        else:
         print(k["name"]+" is a folder\n")
         commonmaster(path+"/"+k["name"], seg) 
       #for k in data["data"]:
        #print(type(k))
        #print(k["name"])
       print("**************************************   END   **************************************")
       #data=response.content()
       #print(type(data))
       #json_object = json.loads(data)
       #json_formatted_str = json.dumps(json_object, indent=2)
       #print(json_formatted_str)
       r = requests.get(url)
   else:
       # If the request is unsuccessful, print the status code and the error message
       print(f'Request failed with status code {response.status_code}: {response.text}')


def commondownload(seg, path , obj):
   print("#########  You are now in Downloading file content   ##########") 
   url = "https://www.devconnect2nse.com/extranet-api/common/content/1.0?segment="+seg+"&folderPath="+path
   #url1 = 'https://www.devconnect2nse.com/extranet-api/logout/1.0'
   #myobj1 = {
   #"memberCode":"90185",
   import requests
   # Replace <TOKEN> with your actual token
   #TOKEN ='eyJhbGciOiJSUzI1NiJ9.eyJtZW1iZXJDZCI6IjkwMTg1Iiwic3ViIjoiOTAxODUiLCJsb2dpbklkIjoiMTQ0NzMiLCJpc3MiOiIxNDQ3MyIsImV4cCI6MTY3MTUzMTEwOCwiaWF0IjoxNjcxNTI3NTA4LCJqdGkiOiIxYjEzYjU1MS1jOGEyLTRkMzUtODVlNi02YWNkMDNiMDRmYWIifQ.fTPnNni_WPGDhMxYSJ1WaOitplwgZPKQsgrt1ZpDsVaev1Pfw_7rgZW6rBXSbHbG8gxHqmwHY24L2Jw3VPL1-w'
   # Set the API endpoint URL
   #url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=CM&folderPath=/Downloads&filename=text.txt
   url ="https://www.connect2nse.com/extranet-api/common/file/download/1.0?segment="+seg+"&folderPath="+path+"&filename="+obj
   #url ='https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=CM&folderPath=&date=18-01-2023'
   #url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment="+seg+"&folderPath="+path+"&filename="+filename
   # Set the headers for the request, including the Authorization header with the token
   headers = {'Authorization': 'Bearer ' + TOKEN}
   # Make the GET request
   response = requests.get(url, headers=headers)
   # Check the status code of the response
   
   if response.status_code == 200:
       # If the request is successful, print the response data
    #print(response.json())
    #request.urlretrieve(url,"/home/akshay/newfile.csv")
    #data=requests.get(url)
    print(response)
    data=response.content
    #print(data)
    print(type(data))
    r = requests.get(url)
    with open("/home/akshay/Downloads/From_api_ftp/CM_COMMON/"+path+"/"+obj, 'wb') as f:
     #line = [data.encode('utf8')]
     f.write(data)
   else:
       # If the request is unsuccessful, print the status code and the error message
       print(f'Request failed with status code {response.status_code}: {response.text}')

def memberlisting(path, seg):
   print("#########  You are now in listing content  ##########")
   list=[]
   import requests
   # Replace <TOKEN> with your actual token
   # Set the API endpoint URL
   url = "https://www.devconnect2nse.com/extranet-api/member/content/1.0?segment="+seg+"&folderPath="+path
   # Set the headers for the request, including the Authorization header with the token
   headers = {'Authorization': 'Bearer ' + TOKEN}
   # Make the GET request
   response = requests.get(url, headers=headers)
   # Check the status code of the response
   if response.status_code == 200:
       data=response.json()
       print(type(data))
       print(data.keys())
       print("************************************   RESPONSE   ************************************")
       for k in data["data"]:
         print(k["name"])
         list.append(k["name"])
       print("**************************************   END   **************************************")
       r = requests.get(url)
   else:
       # If the request is unsuccessful, print the status code and the error message
       print(f'Request failed with status code {response.status_code}: {response.text}')


def membermaster(path, seg):
   print("#########  You are now in master content  ##########") 
   import requests
   # Replace <TOKEN> with your actual token
   # Set the API endpoint URL
   url = "https://www.devconnect2nse.com/extranet-api/member/content/1.0?segment="+seg+"&folderPath="+path
   # Set the headers for the request, including the Authorization header with the token
   headers = {'Authorization': 'Bearer ' + TOKEN}
   # Make the GET request
   response = requests.get(url, headers=headers)
   # Check the status code of the response
   if response.status_code == 200:
       data=response.json()
       print(type(data))
       print(data.keys())
       #print(data["data"].keys())
       print("************************************   RESPONSE   ************************************")
       memberlisting(path, seg)
       if not os.path.isdir("/home/akshay/Downloads/From_api_ftp/"+seg+"_MEMBER/"+path):
        os.mkdir("/home/akshay/Downloads/From_api_ftp/"+seg+"_MEMBER/"+path)
       for k in data["data"]:
        #print(type(k))
        print(path)
        if(k["type"]=='File'):
         print(k["name"]+" is a file\n")
         obj=k["name"]
         path_to_file = "/home/akshay/Downloads/From_api_ftp/"+seg+"_COMMON/"+path+"/"+obj
         check_file = os.path.isfile(path_to_file)
         if check_file == True:
          print(f'The file {path_to_file} exists')
         else:
          print(f'The file {path_to_file} does not exist')
          memberdownload(seg, path, obj)
        else:
         print(k["name"]+" is a folder\n")
         membermaster(path+"/"+k["name"], seg) 
       print("**************************************   END   **************************************")
       r = requests.get(url)
   else:
       # If the request is unsuccessful, print the status code and the error message
       print(f'Request failed with status code {response.status_code}: {response.text}')

def memberdownload(seg, path , obj):
   print("#########  You are now in Downloading file content   ##########") 
   url = "https://www.devconnect2nse.com/extranet-api/member/content/1.0?segment="+seg+"&folderPath="+path
   #url1 = 'https://www.devconnect2nse.com/extranet-api/logout/1.0'
   #myobj1 = {
   #"memberCode":"90185",
   import requests
   #url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=CM&folderPath=/Downloads&filename=text.txt
   url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment="+seg+"&folderPath="+path+"&filename="+obj
   #url ='https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment=CM&folderPath=&date=18-01-2023'
   #url ="https://www.connect2nse.com/extranet-api/member/file/download/1.0?segment="+seg+"&folderPath="+path+"&filename="+filename
   # Set the headers for the request, including the Authorization header with the token
   headers = {'Authorization': 'Bearer ' + TOKEN}
   # Make the GET request
   response = requests.get(url, headers=headers)
   # Check the status code of the response
   
   if response.status_code == 200:
    print(response)
    data=response.content
    #print(data)
    print(type(data))
    r = requests.get(url)
    
    with open("/home/akshay/Downloads/From_api_ftp/"+seg+"_MEMBER/"+path+"/"+obj, 'wb') as f:
     #line = [data.encode('utf8')]
     f.write(data)
   else:
       # If the request is unsuccessful, print the status code and the error message
       print(f'Request failed with status code {response.status_code}: {response.text}')

print("Welcome to FTP Script")
print("Enter 1 to login or 0 to skip it") 
j=input()
print (j)

if j=='1':
   print("##########  UAT ENV logging in  ##########")
   baseurl='https://www.devconnect2nse.com/extranet-api/login/1.0'
   url = 'https://www.devconnect2nse.com/extranet-api/login/1.0'
   myobj = {
   "memberCode":"90185",
   "loginId":"14473",
   "password":"04txjEGPDcrODvVbNOL-QQ=="
   }
   x = requests.post(url, json = myobj)
   print (x)
   print(type(x))
   j=x.json()
   print(j)
   print(j["token"])
   TOKEN=j["token"]
   print("You are now logged in")

j=input("Enter 0 for using api functions\n")

while j=='0':
 print("############# MAIN MENU #############")
 print("Enter 0 to listing common content")
 print("Enter 1 to listing member content")
 print("Enter 2 for downloading common content folders")
 print("Enter 3 to downoading member content folders")
 print("Enter 4 for downloading common content files")
 print("Enter 5 to downoading member content files")

 i=input()
 if i=='2':
   seg=input("Enter Segment\n")
   path=input("Enter path\n")
   commonmaster(path, seg)
   
 if i=='3':
  seg=input("Enter Segment\n")
  path=input("Enter path\n")
  membermaster(path, seg)
  
 if i=='0':
  seg=input("Enter Segment\n")
  path=input("Enter path\n")
  commonlisting(path, seg)
  
 if i=='1':
  seg=input("Enter Segment\n")
  path=input("Enter path\n")
  memberlisting(path, seg)

 if i=='4':
  seg=input("Enter Segment\n")
  path=input("Enter path\n")
  commondownload(path, seg)

 if i=='5':
  seg=input("Enter Segment\n")
  path=input("Enter path\n")
  memberdownload(path, seg)
 
 print("You are now in Main menu")
 print("Press 0 to continue")
 print("Press 5 to exit")
 j=input()

print("You have now exited the code")
