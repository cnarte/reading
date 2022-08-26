from unittest import result
import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
import urllib.request
import os
import json
import upload
import ocr

from ast import arg
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

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

sched  = BackgroundScheduler()

from datetime import datetime

def datetime_to_cron(dt):
  # FYI: not all cron implementations accept the final parameter (year)
  return f"cron({dt.minute} {dt.hour} {dt.day} {dt.month} ? {dt.year})"

@app.get("/")
async def main():
    return {"message": "Hello World"}

from datetime import datetime, timedelta

@app.post("/reading_test")
async def reading(info : Request):
    req_info = await info.json()
    print(dict(req_info))
    try:
        
        link =dict(req_info)["link"] 
        uid = dict(req_info)["uuid"]
        
        urllib.request.urlretrieve(link, 'video_name.mp4') 
        

        sched  = BackgroundScheduler()
        x = datetime.now() #+ timedelta(minutes=3)
        x += timedelta(minutes=10)
        datetime_ = x
        sched.add_job(predict_vid,'cron',day = x.day,hour=x.hour,minute=x.minute,month=x.month,year=x.year,args=['video_name.mp4',uid],coalesce=False)
        # res = predict_vid('video_name.mp4')
        
        sched.print_jobs()
        sched.start()
        # with open("results/"+uid+'.json', 'w') as fp:
        #     json.dump(res, fp)
        if os.path.exists('video_name.mp4'):
            os.remove('video_name.mp4') # one file at a time
        return {"message": "success", "link_recived":link}
    except Exception as e:
        print("problem", e)
        return {"message": "Please check vedio again"}

@app.get("/reading_test_result/{uuid_}")
async def reading_result(uuid_ : int ,info : Request):
    try:
        # id = await info.json()
        uid = uuid_#dict(id)["uuid"]
        dirs =  os.listdir("results")
        path = str(uid)+".json"
        # dirs = [x.split(".")[0] for x in dirs]
        print(dirs)
        if(path in dirs):
            p = os.path.join("results",path)
            f = open(p)
            res = json.load(f)
            return {"results": res}
        else:
            return{"results":"not yet generated"}
    except Exception as e:
        print(e)
        return {"error":e}

@app.get("/ocr_test_result")
async def ocr_result(info : Request):
    try:
        id = await info.json()
        url = dict(id)["link"]
        a,b = ocr.make_pred(url)
        return {"correct":a,"out_of":b}
    except Exception as e:
        print(e)
        return {"error":e}


