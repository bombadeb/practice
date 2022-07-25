from ast import pattern
from typing import Pattern
import requests
import re
from fastapi import FastAPI


import uvicorn
app = FastAPI()

@app.get("/testapi/short/{id}")
def test_short_api(id):
    response = requests.get("https://ionaapp.com/assignment-magic/dk/short/ab")
    if response.status_code == 200:
        if len(id) == 2:
            json_response = response.json()
            print(json_response['uid'])
            if re.fullmatch(r'[0-9a-fA-F]{32}',json_response['uid']):
                return {'Test Result': 'SUCCESS'}
            else:
                return {'Test Result': 'SUCCESS', "Reason": "UID configuration mismatch"}
        else:
            return {'Test Result' : 'FAILURE', 'Reason': 'Value should be 2 characters only'}
    else:
        return {'Test Result' : 'Not 200 Response'}

@app.get("/testapi/long/{id}")
def test_long_api(id):
    response = requests.get("https://ionaapp.com/assignment-magic/dk/short/ab")
    if response.status_code == 200:
        if len(id) == 3:
            json_response = response.json()
            print(json_response['uid'])
            if re.fullmatch(r'[0-9a-fA-F]{32}',json_response['uid']):
                return {'Test Result': 'SUCCESS'}
            else:
                return {'Test Result': 'SUCCESS', "Reason": "UID configuration mismatch"}
        else:
            return {'Test Result' : 'FAILURE', 'Reason': 'Value should be 3 characters only'}
    else:
        return {'Test Result' : 'Not 200 Response'}



if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
