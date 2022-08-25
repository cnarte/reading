from unittest import result
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
import urllib.request
import os
import json

from main import predict_vid
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.post("/reading_test")
async def reading(info : Request):
    req_info = await info.json()
    print(dict(req_info))
    try:
        
        link =dict(req_info)["link"] 
        uid = dict(req_info)["uuid"]
        
        urllib.request.urlretrieve(link, 'video_name.mp4') 
        
        res = await predict_vid('video_name.mp4')
        
        with open("results/"+uid+'.json', 'w') as fp:
            json.dump(res, fp)
        if os.path.exists('video_name.mp4'):
            os.remove('video_name.mp4') # one file at a time
        return {"message": "success", "link_recived":link}
    except Exception as e:
        print("problem", e)
        return {"message": "Please check vedio again"}

@app.get("/reading_test_result")
async def reading_result(info : Request):
    id = await info.json()
    uid = dict(id)["uuid"]
    dirs =  os.listdir("results")
    path = uid+".json"
    # dirs = [x.split(".")[0] for x in dirs]
    print(dirs)
    if(path in dirs):
        p = os.path.join("results",path)
        f = open(p)
        
        res = json.load(f)
        return {"results": res}
    else:
        return{"results":"not yet generated"}