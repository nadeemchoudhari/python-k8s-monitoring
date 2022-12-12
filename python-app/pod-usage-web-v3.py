#!/usr/bin/python3

#from flask_restful import Api, Resource
from json2html import *
import sys
import time
#import requests
import json
import os
import subprocess                    



######################################################

original_stdout = sys.stdout # Save a reference to the original standard output

myToken = os.environ["TOKEN"]

data1 = "Authorization: Bearer "
data2 = myToken
data3 = data1 + data2


######## LOAD DATA FROM METRICS SERVER USING CURL COMMAND WITH SERVICE ACCOUNT TOKEN 
def checkData():
        data1 = "Authorization: Bearer "
        data2 = myToken
        data3 = data1 + data2

        response = []

        response = json.loads(subprocess.check_output([
            'curl',
             '-s',
            '-X',
            'GET',
            'https://kubernetes.docker.internal:6443/apis/metrics.k8s.io/v1beta1/pods',
            '--header',
            data3,
            '--insecure',
    
        ]))

        return response

##### TABULATE index.html output 

run = 1
it = 0
while run == 1 :

    data = checkData()
    
    df = json2html.convert(json = data)
    open('/web/html/index.html', 'w').close()
    with open('/web/html/index.html', 'a') as f:
       sys.stdout = f
       print('iteration=', it)
       print(df)
                

    it = it + 1        
    time.sleep(2)



















