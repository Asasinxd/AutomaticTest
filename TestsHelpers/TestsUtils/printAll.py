from json import dumps
from time import time, localtime, asctime
from os import getenv
import curlify

def tryPrintJson(name, data):
    try:
        print(f"{name}: " , dumps(data, indent = 4))
    except:
        print(f"{name}: {data}")

def printAll(name = "", response = "", data = ""):
    curl = getenv('printCurl')
    if curl == None:    
        curl = False

    print("\n\n\n", name)
    print("Time: ", asctime(localtime(time())))
    if curl:
        print("Request: " , curlify.to_curl(response.request))
    else:
        print("Method: " , response.request.method)
        print("Url: " , response.request.url)
        tryPrintJson("Data", data)
        print("Headers: " , dumps(dict(response.request.headers), indent = 4))
    print("StatusCode: " , response.status_code)
    try:
        print("Response: " , dumps(response.json(), indent = 4))
    except:
        print("Response: " , response.text)