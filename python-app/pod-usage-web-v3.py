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
        

        response = []

        response = json.loads(subprocess.check_output([
            'curl',
             '-s',
            '-X',
            'GET',
            'https://kubernetes.default.svc:443/apis/metrics.k8s.io/v1beta1/pods',
            '--header',
            data3,
            '--insecure',
    
        ]))

        return response

### Load Information from kubernetes api server for pod status 
def checkData2():
        

        response = []

        response = json.loads(subprocess.check_output([
            'curl',
             '-s',
            '-X',
            'GET',
            'https://kubernetes.default.svc:443/api/v1/pods',
            '--header',
            data3,
            '--insecure',
    
        ])) 

        return response["items"]

##### TABULATE index.html output 

run = 1
it = 0
while run == 1 :
    data = checkData()
    data2 = checkData2()

    open('/web/html/index.html', 'w').close()
    with open('/web/html/index.html', 'a') as f:
            sys.stdout = f
            
            print('<h1>PYTHON MONITORING</h1>')
            
    df = json2html.convert(json = data)
    
    with open('/web/html/index.html', 'a') as f:
       sys.stdout = f
       print("\n",'<h2> POD USAGES :</h2>')
       print('iteration=', it, "\n")
       
       print(df)

    time.sleep(1)

    with open('/web/html/index.html', 'a') as f:
            sys.stdout = f
            print("\n",'<h2> POD STATUS :</h2>')


            for item in data2:
                df2 = json2html.convert(json = item["status"])
        
                phase = json2html.convert(json = item["status"]['phase'])
                condition = json2html.convert(json = item["status"]['conditions'])
                status = json2html.convert(json = item["status"]['containerStatuses'])

                
                print("\n",'<h3> STATUS: ',phase,'</h2>',"\n",condition,"\n",status)
                print('<br><br>')
                
    time.sleep(1)
    it = it + 1        
    



















