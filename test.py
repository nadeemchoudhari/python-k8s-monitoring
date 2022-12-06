#!/usr/bin/python3


import subprocess


#myToken = str(subprocess.check_output( ["kubectl", "get", "secret", "serviceaccount-sa-token" , "-o" , "jsonpath='{.data.token}'" ,"|", "base64" , "--decode"]))

myToken = str(subprocess.check_output( ["kubectl", "get", "secret", "serviceaccount-sa-token" , "-o" , "jsonpath='{.data.token}'"]))

token = subprocess.check_output(["echo", myToken , "|" , "base64" , "--decode" ])

#response = "xyz"
#command = str("echo " + response + " |" + " jq")

print(token)

