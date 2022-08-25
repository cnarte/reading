from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
import urllib.request
import os

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
        
        urllib.request.urlretrieve(link, 'video_name.mp4') 
        res = await predict_vid('video_name.mp4')
        if os.path.exists('video_name.mp4'):
            os.remove('video_name.mp4') # one file at a time
        return {"message": "success", "link_recived":link}
    except Exception as e:
        print("problem", e)
        return {"message": "Please check vedio again"}


