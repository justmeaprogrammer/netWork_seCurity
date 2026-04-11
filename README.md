<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:0284c7,100:16a34a&height=240&section=header&text=Network%20Security&fontSize=52&fontColor=ffffff&animation=fadeIn&fontAlignY=40&desc=Phishing%20Website%20Detection%20Pipeline&descAlignY=62" alt="Network Security banner" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Scikit--Learn-1d4ed8?style=for-the-badge&logo=python&logoColor=white" alt="Python and scikit-learn" />
  <img src="https://img.shields.io/badge/MongoDB-Data%20Source-15803d?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB" />
  <img src="https://img.shields.io/badge/Pipeline-Ingestion%20to%20Training-0f172a?style=for-the-badge" alt="Pipeline" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Artifacts-Timestamped-f97316?style=flat-square" alt="Artifacts" />
  <img src="https://img.shields.io/badge/Validation-Schema%20%2B%20Drift-0284c7?style=flat-square" alt="Validation" />
  <img src="https://img.shields.io/badge/Models-5%20Classifiers-16a34a?style=flat-square" alt="Models" />
</p>

# Network Security

This project builds a phishing website detection pipeline using MongoDB, scikit-learn, and a local artifact-based training workflow.

The current codebase supports:

- loading phishing records from [`Network_data/phisingData.csv`](/home/om/ML_PROJECTS/NetworkSecurity/Network_data/phisingData.csv)
- pushing the dataset into MongoDB with [`push_data.py`](/home/om/ML_PROJECTS/NetworkSecurity/push_data.py)
- exporting data from MongoDB into a feature store
- splitting the dataset into train and test CSV files
- validating schema consistency and train/test drift
- transforming data with `KNNImputer`
- training multiple classification models and saving the best trained model
- serving the trained model through FastAPI in [`app.py`](/home/om/ML_PROJECTS/NetworkSecurity/app.py)
- running batch prediction by uploading the validated file [`valid_data/test.csv`](/home/om/ML_PROJECTS/NetworkSecurity/valid_data/test.csv)

## Visual Overview

<p align="center">
  <img src="https://quickchart.io/graphviz?format=png&width=1200&graph=digraph%20G%20%7B%20rankdir%3DLR%3B%20node%20%5Bshape%3Dbox%20style%3D%22rounded%2Cfilled%22%20fontname%3DHelvetica%5D%3B%20csv%20%5Blabel%3D%22CSV%20Dataset%0AphisingData.csv%22%20fillcolor%3D%22%23dbeafe%22%20color%3D%22%232563eb%22%5D%3B%20mongo%20%5Blabel%3D%22MongoDB%0AOmKulkarni.NetworkData%22%20fillcolor%3D%22%23dcfce7%22%20color%3D%22%2316a34a%22%5D%3B%20ingest%20%5Blabel%3D%22Data%20Ingestion%0Afeature%20store%20%2B%20split%22%20fillcolor%3D%22%23e0f2fe%22%20color%3D%22%230284c7%22%5D%3B%20valid%20%5Blabel%3D%22Data%20Validation%0Aschema%20%2B%20drift%22%20fillcolor%3D%22%23ffedd5%22%20color%3D%22%23f97316%22%5D%3B%20transform%20%5Blabel%3D%22Data%20Transformation%0AKNNImputer%20%2B%20npy%22%20fillcolor%3D%22%23ede9fe%22%20color%3D%22%237c3aed%22%5D%3B%20train%20%5Blabel%3D%22Model%20Training%0AGridSearchCV%20%2B%20model.pkl%22%20fillcolor%3D%22%23e2e8f0%22%20color%3D%22%23334155%22%5D%3B%20csv%20-%3E%20mongo%20-%3E%20ingest%20-%3E%20valid%20-%3E%20transform%20-%3E%20train%3B%20%7D" alt="Pipeline overview" />
</p>

## Pipeline

The main workflow in [`main.py`](/home/om/ML_PROJECTS/NetworkSecurity/main.py) runs these stages in sequence:

1. Data ingestion
2. Data validation
3. Data transformation
4. Model training

At a high level, the flow is:

```text
CSV dataset
  |
  v
push_data.py
  |
  v
MongoDB
  |
  v
DataIngestion
  |
  v
DataValidation
  |
  v
DataTransformation
  |
  v
ModelTrainer
```

## What Each Stage Does

### Data ingestion

Implemented in [`networksecurity/components/data_ingestion.py`](/home/om/ML_PROJECTS/NetworkSecurity/networksecurity/components/data_ingestion.py).

- connects to MongoDB using `MONGO_DB_URL`
- reads the `NetworkData` collection from the `OmKulkarni` database
- drops MongoDB `_id`
- replaces `"na"` with `NaN`
- saves a feature-store CSV
- creates `train.csv` and `test.csv`

### Data validation

Implemented in [`networksecurity/components/data_validation.py`](/home/om/ML_PROJECTS/NetworkSecurity/networksecurity/components/data_validation.py).

- checks the expected number of columns using [`data_schema/schema.yaml`](/home/om/ML_PROJECTS/NetworkSecurity/data_schema/schema.yaml)
- compares train and test distributions with `ks_2samp`
- writes a drift report YAML file
- stores validated train and test data when validation succeeds

### Data transformation

Implemented in [`networksecurity/components/data_transformation.py`](/home/om/ML_PROJECTS/NetworkSecurity/networksecurity/components/data_transformation.py).

- separates features from the target column `Result`
- converts target label `-1` to `0`
- imputes missing values with `KNNImputer`
- saves transformed train and test arrays as `.npy`
- saves the fitted preprocessing object as `preprocessing.pkl`

### Model training

Implemented in [`networksecurity/components/model_trainer.py`](/home/om/ML_PROJECTS/NetworkSecurity/networksecurity/components/model_trainer.py).

- loads transformed NumPy arrays
- trains and evaluates:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - AdaBoost
  - Gradient Boosting
- tunes supported models with `GridSearchCV`
- selects the best model by test accuracy
- wraps the fitted preprocessor and model inside `NetworkModel`
- saves the trained model artifact as `model.pkl`

### Batch prediction

Implemented in [`app.py`](/home/om/ML_PROJECTS/NetworkSecurity/app.py).

- exposes `POST /predict` for CSV upload
- loads the saved model from [`final_models/model.pkl`](/home/om/ML_PROJECTS/NetworkSecurity/final_models/model.pkl)
- loads the saved preprocessor from [`final_models/preprocesor.pkl`](/home/om/ML_PROJECTS/NetworkSecurity/final_models/preprocesor.pkl)
- uses the validated feature-only batch file [`valid_data/test.csv`](/home/om/ML_PROJECTS/NetworkSecurity/valid_data/test.csv)
- appends a `predicted_column` to the uploaded data
- saves the prediction result to [`prediction_output/prediction.csv`](/home/om/ML_PROJECTS/NetworkSecurity/prediction_output/prediction.csv)
- renders the predicted rows in the browser through [`templates/table.html`](/home/om/ML_PROJECTS/NetworkSecurity/templates/table.html)

## Project Structure

```text
NetworkSecurity/
|-- app.py
|-- Network_data/
|   `-- phisingData.csv
|-- data_schema/
|   `-- schema.yaml
|-- final_models/
|   |-- model.pkl
|   `-- preprocesor.pkl
|-- networksecurity/
|   |-- cloud/
|   |-- components/
|   |   |-- data_ingestion.py
|   |   |-- data_transformation.py
|   |   |-- data_validation.py
|   |   `-- model_trainer.py
|   |-- constant/
|   |   `-- trainig_pipeline/
|   |       `-- __init__.py
|   |-- entity/
|   |   |-- artifact_entity.py
|   |   `-- config_entity.py
|   |-- exception/
|   |   `-- exception.py
|   |-- logging/
|   |   `-- logger.py
|   `-- utils/
|       |-- main_utils/
|       |   `-- utils.py
|       `-- ml_utils/
|           |-- metric/
|           |   `-- classification_metric.py
|           `-- model/
|               `-- estimator.py
|-- prediction_output/
|   `-- prediction.csv
|-- templates/
|   `-- table.html
|-- valid_data/
|   `-- test.csv
|-- main.py
|-- push_data.py
|-- requirements.txt
|-- setup.py
`-- test_monogdb.py
```

## Dataset Schema

The schema is defined in [`data_schema/schema.yaml`](/home/om/ML_PROJECTS/NetworkSecurity/data_schema/schema.yaml).

- total columns: 31
- target column: `Result`
- all columns are currently treated as numerical inputs in the schema file
- batch prediction uses the validated 30 feature columns from [`valid_data/test.csv`](/home/om/ML_PROJECTS/NetworkSecurity/valid_data/test.csv)

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

Optional editable install:

```bash
pip install -e .
```

### 2. Create `.env`

Create a `.env` file in the project root:

```env
MONGO_DB_URL="your_mongodb_connection_string"
```

### 3. Push the CSV dataset to MongoDB

```bash
python push_data.py
```

This loads [`Network_data/phisingData.csv`](/home/om/ML_PROJECTS/NetworkSecurity/Network_data/phisingData.csv) into:

- database: `OmKulkarni`
- collection: `NetworkData`

### 4. Run the full pipeline

```bash
python main.py
```

### 5. Start the FastAPI app

```bash
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000/docs` to access the Swagger UI.

### 6. Run batch prediction

Use the `POST /predict` endpoint and upload:

- [`valid_data/test.csv`](/home/om/ML_PROJECTS/NetworkSecurity/valid_data/test.csv)

This validated CSV is the ready-to-use batch input file for prediction.

## Artifacts Produced

The pipeline creates timestamped folders under `Artifacts/`, including outputs such as:

- `data_ingestion/feature_store/phisingData.csv`
- `data_ingestion/ingested/train.csv`
- `data_ingestion/ingested/test.csv`
- `data_validation/validated/train.csv`
- `data_validation/validated/test.csv`
- `data_validation/drift_report/report.yaml`
- `data_transformation/transformed/train.npy`
- `data_transformation/transformed/test.npy`
- `data_transformation/transformed/transformed_object/preprocessing.pkl`
- `model_trainer/trained_model/model.pkl`
- `prediction_output/prediction.csv`

Logs are also written under `logs/`.

## API Endpoints

The FastAPI app in [`app.py`](/home/om/ML_PROJECTS/NetworkSecurity/app.py) exposes:

- `GET /`: redirects to Swagger docs
- `GET /train`: runs the full training pipeline
- `POST /predict`: accepts a batch CSV upload and returns the predicted table

For batch prediction, the recommended upload file is [`valid_data/test.csv`](/home/om/ML_PROJECTS/NetworkSecurity/valid_data/test.csv).

## Training Snapshot

<p align="center">
  <img src="https://quickchart.io/graphviz?format=png&width=1200&graph=digraph%20G%20%7B%20rankdir%3DLR%3B%20node%20%5Bshape%3Dbox%20style%3D%22rounded%2Cfilled%22%20fontname%3DHelvetica%5D%3B%20arr%20%5Blabel%3D%22Transformed%20Arrays%0Atrain.npy%20%2B%20test.npy%22%20fillcolor%3D%22%23dbeafe%22%20color%3D%22%232563eb%22%5D%3B%20imputer%20%5Blabel%3D%22Preprocessing%0AKNNImputer%20Pipeline%22%20fillcolor%3D%22%23dcfce7%22%20color%3D%22%2316a34a%22%5D%3B%20models%20%5Blabel%3D%22Candidate%20Models%0ALR%20%7C%20DT%20%7C%20RF%20%7C%20AdaBoost%20%7C%20GB%22%20fillcolor%3D%22%23ffedd5%22%20color%3D%22%23f97316%22%5D%3B%20search%20%5Blabel%3D%22GridSearchCV%0Amodel%20selection%22%20fillcolor%3D%22%23ede9fe%22%20color%3D%22%237c3aed%22%5D%3B%20saved%20%5Blabel%3D%22Saved%20Artifact%0ANetworkModel%20-%3E%20model.pkl%22%20fillcolor%3D%22%23e2e8f0%22%20color%3D%22%23334155%22%5D%3B%20arr%20-%3E%20imputer%20-%3E%20models%20-%3E%20search%20-%3E%20saved%3B%20%7D" alt="Model training stack" />
</p>

## Important Files

- [`app.py`](/home/om/ML_PROJECTS/NetworkSecurity/app.py): FastAPI app for training and batch prediction
- [`main.py`](/home/om/ML_PROJECTS/NetworkSecurity/main.py): runs the full training pipeline
- [`push_data.py`](/home/om/ML_PROJECTS/NetworkSecurity/push_data.py): uploads CSV records to MongoDB
- [`valid_data/test.csv`](/home/om/ML_PROJECTS/NetworkSecurity/valid_data/test.csv): validated batch input file used for prediction uploads
- [`prediction_output/prediction.csv`](/home/om/ML_PROJECTS/NetworkSecurity/prediction_output/prediction.csv): saved batch prediction output
- [`networksecurity/entity/config_entity.py`](/home/om/ML_PROJECTS/NetworkSecurity/networksecurity/entity/config_entity.py): builds artifact paths and stage configs
- [`networksecurity/entity/artifact_entity.py`](/home/om/ML_PROJECTS/NetworkSecurity/networksecurity/entity/artifact_entity.py): defines stage artifact dataclasses
- [`networksecurity/utils/main_utils/utils.py`](/home/om/ML_PROJECTS/NetworkSecurity/networksecurity/utils/main_utils/utils.py): YAML, pickle, NumPy, and model-evaluation helpers

## Notes

- The codebase uses existing names such as `phisingData.csv`, `trainig_pipeline`, and `test_monogdb.py`; those spellings are preserved because the code depends on them.
- [`Dockerfile`](/home/om/ML_PROJECTS/NetworkSecurity/Dockerfile) is currently empty.
- The logging setup in [`networksecurity/logging/logger.py`](/home/om/ML_PROJECTS/NetworkSecurity/networksecurity/logging/logger.py) creates a timestamped log path under `logs/`.
- The repo includes a MongoDB connection sample in [`test_monogdb.py`](/home/om/ML_PROJECTS/NetworkSecurity/test_monogdb.py).

## Author

Om Kulkarni
