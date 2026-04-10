import sys

from networksecurity.exception.exception import NetworkSecurityException

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse


app=FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/",tags=['authentication'])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        from networksecurity.pipeline.training_pipeline import TrainingPipeline

        train_pipeline=TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training is successfull")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
    
if __name__=="__main__":
    app_run(app,host="localhost",port=8000)
