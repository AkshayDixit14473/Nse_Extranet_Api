# **Nse_Extranet_Api**

National Stock Exchange is going to introduce a brand new api for its members . This api would be use to access common and member files of different segments. In this repository, codes to automaticaly download chosen files is present. A user interface has also been designed through code to use all the features available through the api.

Before trying to make code, please make sure all prerequisites are completed according to the circulars MSD 54667 and MSD 55065. After making a user id, assigning roles and generating secret key, you would need to encrpt the key in AES256 encyption. Then this encrypted key can be used for login through a json object.

>**AE256_encrypt** consists of a code that can be used to convert your secret key into your encrypted key.

>**MSD 54667** contains circulars about UAT Environment

>**MSD 55065** contains circular about LIVE Environment

>**api_uat_master** consists of code to work on Test/UAT Environment

>**api_master** consists of code to work on live Environment

>**ftp_cm_auto_yesterday.py** conisist of code that downloads yesterday's files of live cm segment automatically on execution

>**ftp_fo_auto_yesterday.py** conisist of code that downloads yesterday's files of live fo segment automatically on execution

>**ftp_cm_shilpi_manual.py** consist of code which gives manual control over live cm segment functions

>**ftp_fo_shilpi_manual.py** consist of code which gives manual control over live fo segment functions

