#### This is the main driver script ####

import subprocess
import sys,time
import pickle
from ibm_watson_machine_learning import APIClient

sys.path.insert(0,'/home/wmlfuser/.local/lib/python3.7/site-packages/')
sys.path.insert(0, './')


# Setup Client
username = 'anindyos'
password = 'password'
url = 'https://cpd35-cpd-cpd35.ap-zen3-4ae72ace414f5ac321fce2db38ce35cc-0000.au-syd.containers.appdomain.cloud'

wml_credentials = {
    "username": username,
    "password": password,
    "url": url,
    "instance_id": 'openshift',
    "version": '3.5'
}
client = APIClient(wml_credentials)
space_id = 'f6120d27-b321-4704-90f5-0b1a890603bd'
client.set.default_space(space_id)

#Download Required Files locally
client.data_assets.download("17efefbf-51d1-42e1-bd10-719b83ccb630","my_scripts.zip")

# Unzip files
def unzipfiles():

    # importing required modules 
    from zipfile import ZipFile 

    # specifying the zip file name 
    file_name = "my_scripts.zip"

    # opening the zip file in READ mode 
    with ZipFile(file_name, 'r') as zip: 
        # printing all the contents of the zip file 
        zip.printdir() 

        # extracting all the files 
        print('Extracting all the files now...') 
        zip.extractall() 
        print('Done!') 

    return None

# Call Scripts 

print('This is the main script')
unzipfiles()
exec(open("Subdirectory/subdirscript1.py").read())
exec(open("Subdirectory/subdirscript2.py").read())




