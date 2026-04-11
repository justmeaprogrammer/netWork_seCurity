import os
import sys
import pandas as pd

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.utils.main_utils.utils import load_object, read_yaml_file
from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from networksecurity.constant.trainig_pipeline import TARGET_COLUMN, SCHEMA_FILE_PATH

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,File,UploadFile,Request,HTTPException
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

from fastapi.templating import Jinja2Templates
templates=Jinja2Templates(directory="./templates")


def _get_batch_feature_frame(dataframe: pd.DataFrame) -> pd.DataFrame:
    schema_config = read_yaml_file(SCHEMA_FILE_PATH)
    expected_columns = [
        list(column.keys())[0]
        for column in schema_config["columns"]
        if list(column.keys())[0] != TARGET_COLUMN
    ]

    missing_columns = [column for column in expected_columns if column not in dataframe.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns for prediction: {missing_columns}")

    # Accept both feature-only CSVs and labelled CSVs uploaded for convenience.
    return dataframe.loc[:, expected_columns]


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
    
@app.post("/predict")
async def predict_route(request:Request,file:UploadFile=File(...)):
    try:
        df=pd.read_csv(file.file)
        feature_df=_get_batch_feature_frame(df)
        model=load_object("final_models/model.pkl")
        preprocessor=load_object("final_models/preprocesor.pkl")
        network_model=NetworkModel(preprocessor=preprocessor,model=model)
        y_pred=network_model.predict(feature_df)
        df['predicted_column']=y_pred
        os.makedirs("prediction_output", exist_ok=True)
        df.to_csv("prediction_output/prediction.csv", index=False)
        table_html=df.to_html(classes='table table-striped')
        return templates.TemplateResponse(
            request=request,
            name="table.html",
            context={"table": table_html},
        )
        

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
if __name__=="__main__":
    app_run(app,host="localhost",port=8000)
