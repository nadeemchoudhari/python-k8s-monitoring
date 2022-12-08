#!/usr/bin/python3

#from flask_restful import Api, Resource
import http.server
import socketserver
import sys
import time
#import requests
import json
import os
from kubernetes import client, config 

from kubernetes.config import load_kube_config                     

import subprocess

######################################################

original_stdout = sys.stdout # Save a reference to the original standard output

myToken = os.environ["TOKEN"]

print('mytoken=',  myToken )


#myToken = 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImM1aFVEWEJwSl9Wc3dHUW02Qm5jd3JDdnQ0OVlJbWVpUVFMS041ZGdVWDAifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6InNlcnZpY2VhY2NvdW50LXNhLXRva2VuIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6InNlcnZpY2VhY2NvdW50LXNhIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiZDU2NDIyMWEtMTMwNC00NDk5LWI3ZmItZTdiMTc4ODBmZGJmIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlZmF1bHQ6c2VydmljZWFjY291bnQtc2EifQ.thHpwvvbSsFFeMB5LUmMP5dSYNOIOIzVOtN-oRbOV14fVd5OLHqwNkCNaWfpMZet24J3D21QtfMIXeNSXmOmfJORLw836r2sXt2IdQ9Sa65mgH0_5YA2mLkkd45zYPQhD-CgxVdjzjKR2TK6GvWX4kejE5napP7aAivtpCyLagRIrw9fQZ7ucYZIwBdnu1XajI8tLGCtWiQ859ydCHmwCkJR_ljU-MULMYXM8fAiC-fjny7BY7oXnVEJ5p_Glz_o8dc_dHhDfv70cImuB2u0XmPYT8hmHN9YqX3ZHaAbw9iicV7IHhojorRwRXh6FoooNZlt09kflVsPIe6js2r6Zg'

data1 = "Authorization: Bearer "
data2 = myToken
data3 = data1 + data2


#config.load_kube_config()


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
            'https://E6D4937EC037B44A437F1AF68DCF9AB1.gr7.ap-south-1.eks.amazonaws.com/apis/metrics.k8s.io/v1beta1/pods',
            '--header',
            data3,
            '--insecure',
    
        ]))

        return response["items"]

#### HTTP WEBSERVER FUNCTION




        

run = 1
while run == 1 :

        
    data = checkData()

      


    def table(key, value , cont = '', containername = '', cpu = '', mem = ''):

        

        if cont == "yes" :

            
                
            
            print('<table border=1>')
            #print('<tr><td>',key,'</td><td>',value,'</td></tr>')
            print('<tr><td>Container</td><td>',containername,'</td><td>CPU</td><td>',cpu,'</td><td>MEM</td><td>',mem,'</td></tr>')
            print('</table>')

        elif key == "PODs-name" :

                        print("<table border=1>")
                        print('<tr><td>',key,'</td><td>',value,'</td></tr>')
                        print('</table>')
                        print('<table border=1>')
                        print('<tr><td>Container-Usage</td></tr>')





        else:
                        #print("\n",key ,":", value)

                        print("<table border=1>")
                        print('<tr><td>',key,'</td><td>',value,'</td></tr>')
                        print('</table>')



    medata = {}
    podname = []
    namespace = []
    vtimes = []
    container = []
    cpuusage = []
    memusage = []
    dict = {}

        
        # Looping through each item in the json input
    i = 0
    open('index.html', 'w').close()
    with open('index.html', 'a') as f:
        sys.stdout = f
        for item in data :
 
            vtimes = str(item["timestamp"])
            podname =  item['metadata']['name']
            namespace = item['metadata']['namespace']
    
            dict['NAMESPACE'] = namespace
            dict['PODs-name'] = podname
            dict['timestamp'] = vtimes
    
    
            for key, value in dict.items():

                if key == "NAMESPACE":
                     
                        

                        print("--------------------------\n")
                        table(key, value)
    
                elif key == "PODs-name" :
                    
                        
                    table(key,value)
                    
                
                    for itemc in item["containers"]:

                        

                        containername = itemc['name']

                        cpu  = itemc['usage']['cpu']
                        mem = itemc['usage']['memory']

                        cont = "yes"
                        
                        table(key,value,cont,containername,cpu, mem)
                      
                       # print( ' ' + containername  + ':' + ' cpuusage = ' + cpu + ' ; memusage = '+ mem ) 



        
                else: 
                    
                        table(key, value)
                        
                             
        i = i + 1
        sys.stdout = original_stdout               

    
    time.sleep(8)

    class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.path = '/index.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

    Handler = MyRequestHandler
    server = socketserver.TCPServer(('0.0.0.0', 8000), Handler)
    server.serve_forever()


#with open('filename.txt', 'w') as f:
#    sys.stdout = f # Change the standard output to the file we created.
#    print('This message will be written to a file.')
#    sys.stdout = original_stdout            


    

#config.load_kube_config()
#session = requests.Session()
#session.verify = False

















