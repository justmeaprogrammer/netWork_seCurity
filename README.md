<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,40:0ea5e9,100:22c55e&height=220&section=header&text=Network%20Security&fontSize=48&fontColor=ffffff&animation=fadeIn&fontAlignY=40&desc=Phishing%20Data%20Ingestion%20Pipeline&descAlignY=62" alt="Network Security Banner" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/MongoDB-Database-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit Learn" />
  <img src="https://img.shields.io/badge/Status-Ingestion%20Stage-0EA5E9?style=for-the-badge" alt="Status" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Project%20Focus-Phishing%20Detection%20Pipeline-111827?style=flat-square" alt="Project Focus" />
  <img src="https://img.shields.io/badge/Current%20Module-Data%20Transformation-16A34A?style=flat-square" alt="Current Module" />
  <img src="https://img.shields.io/badge/Logs-Custom%20Tracking-E11D48?style=flat-square" alt="Logs" />
</p>

# Network Security

A beginner-friendly machine learning project for phishing data ingestion and pipeline setup.

This repository currently focuses on the first core stage of the project:

- loading phishing data from a CSV file
- pushing that data into MongoDB
- reading the data back from MongoDB
- saving a feature-store copy
- splitting the dataset into train and test files
- validating the generated train and test files
- checking basic schema consistency and dataset drift
- transforming validated train and test data into NumPy arrays
- saving the fitted preprocessing object for later model stages

## Visual Overview

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:111827,50:0ea5e9,100:22c55e&height=120&section=header&text=CSV%20%E2%86%92%20MongoDB%20%E2%86%92%20DataFrame%20%E2%86%92%20Feature%20Store%20%E2%86%92%20Train%20/%20Test&fontSize=26&fontColor=ffffff" alt="Pipeline Flow" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/1-CSV%20Data-2563EB?style=for-the-badge" alt="CSV Data" />
  <img src="https://img.shields.io/badge/2-MongoDB-059669?style=for-the-badge" alt="MongoDB Step" />
  <img src="https://img.shields.io/badge/3-Pandas%20DataFrame-7C3AED?style=for-the-badge" alt="DataFrame Step" />
  <img src="https://img.shields.io/badge/4-Train%20%2F%20Test-EA580C?style=for-the-badge" alt="Train Test Step" />
</p>

## Current Progress

The project work completed so far includes:

- project package structure created under `networksecurity/`
- custom logging setup added
- custom exception handling added
- pipeline constants defined
- configuration classes created
- data ingestion component implemented
- data validation component implemented
- data transformation component implemented
- MongoDB upload utility added
- train/test data export flow connected through `main.py`
- schema-based column count validation added
- drift report generation added
- validated train/test output flow connected through `main.py`
- transformed train/test NumPy output flow connected through `main.py`


## Project Flow

The current flow of the project is:

1. Read phishing data from `Network_data/phisingData.csv`
2. Upload records into MongoDB using `push_data.py`
3. Start the ingestion pipeline from `main.py`
4. Read the collection from MongoDB into a pandas DataFrame
5. Save the full dataset into the feature store
6. Split the data into train and test sets
7. Validate the train and test files using the schema
8. Check train vs test drift using `ks_2samp`
9. Save validated files and drift report inside the `Artifacts/` directory
10. Transform validated train and test data using `KNNImputer`
11. Save `train.npy`, `test.npy`, and the preprocessing object

## Project Structure

```text
NetworkSecurity/
├── Network_data/
│   └── phisingData.csv
├── networksecurity/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   └── data_transformation.py
│   ├── constant/
│   │   └── trainig_pipeline/
│   │       └── __init__.py
│   ├── entity/
│   │   ├── artifact_entity.py
│   │   └── config_entity.py
│   ├── exception/
│   │   └── exception.py
│   ├── utils/
│   │   └── main_utils/
│   │       └── utils.py
│   └── logging/
│       └── logger.py
├── data_schema/
│   └── schema.yaml
├── main.py
├── push_data.py
├── requirements.txt
└── setup.py
```

## Main Files

### `main.py`

This is the entry point of the project. It creates the config objects, starts the data ingestion process, and prints the ingestion artifact.

### `push_data.py`

This file is used to:

- read the phishing CSV file
- convert it into JSON-like records
- insert those records into MongoDB

### `networksecurity/components/data_ingestion.py`

This file contains the `DataIngestion` class, which:

- connects to MongoDB
- reads collection data into a DataFrame
- saves the feature-store CSV
- splits data into train and test files

### `networksecurity/components/data_validation.py`

This file contains the `DataValidation` class, which:

- reads the generated train and test CSV files
- validates the expected number of columns using `data_schema/schema.yaml`
- checks dataset drift with the Kolmogorov-Smirnov test
- writes a drift report file
- saves validated train and test files

### `networksecurity/components/data_transformation.py`

This file contains the `DataTransformation` class, which:

- reads the validated train and test CSV files
- separates input features and target column
- applies `KNNImputer` through a scikit-learn `Pipeline`
- transforms the train and test feature sets
- saves transformed arrays as `train.npy` and `test.npy`
- saves the fitted preprocessing object for reuse

### `networksecurity/entity/config_entity.py`

This file contains config classes:

- `TrainingPipelineConfig`
- `DataIngestionConfig`

These classes prepare folder paths, file paths, database names, and split settings.

### `networksecurity/entity/artifact_entity.py`

This file contains:

- `DataIngestionArtifact` for train and test output paths
- `DataValidationArtifact` for validation outputs and drift report path
- `DataTransformationArtifact` for transformed NumPy files and preprocessing object path

### `networksecurity/constant/trainig_pipeline/__init__.py`

This file stores project constants such as:

- artifact folder names
- file names
- MongoDB collection name
- MongoDB database name
- train-test split ratio
- schema file path
- data validation output folder names
- data transformation output folder names and file names

### `data_schema/schema.yaml`

This schema file stores:

- expected dataset columns
- numerical columns used by the pipeline

### `networksecurity/utils/main_utils/utils.py`

This utility file contains helper functions for:

- reading YAML files
- writing YAML reports
- saving NumPy arrays
- saving serialized Python objects

### `networksecurity/logging/logger.py`

This file sets up logging so project activity is written into log files.

### `networksecurity/exception/exception.py`

This file defines a custom exception class to make errors easier to trace.

## Tech Stack

The project currently uses:

- Python
- Pandas
- NumPy
- Scikit-learn
- MongoDB
- PyMongo
- python-dotenv

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,mongodb,git,github,vscode" alt="Tech Stack Icons" />
</p>

## Setup

### 1. Create and activate your environment

Install the required packages:

```bash
pip install -r requirements.txt
```

### 2. Add environment variables

Create a `.env` file and add:

```env
MONGO_DB_URL="your_mongodb_connection_string"
```

### 3. Push data to MongoDB

```bash
python push_data.py
```

### 4. Run the pipeline

```bash
python main.py
```

## Output

After running the pipeline, the project creates:

- feature-store CSV file
- train CSV file
- test CSV file
- validated train CSV file
- validated test CSV file
- drift report YAML file
- transformed train NumPy file
- transformed test NumPy file
- preprocessing object file
- log files
- timestamp-based artifact folders

## Simple Architecture

```text
Raw CSV
  |
  v
push_data.py
  |
  v
MongoDB Collection
  |
  v
DataIngestion
  |
  +--> feature_store/phisingData.csv
  |
  +--> ingested/train.csv
  |
  +--> ingested/test.csv
  |
  v
DataValidation
  |
  +--> validated/train.csv
  |
  +--> validated/test.csv
  |
  +--> drift_report/report.yaml
  |
  v
DataTransformation
  |
  +--> transformed/train.npy
  |
  +--> transformed/test.npy
  |
  +--> transformed/transformed_object/preprocessing.pkl
```

## What Is Implemented So Far

Completed:

- ingestion pipeline skeleton
- MongoDB connection flow
- feature store export
- train-test split export
- schema-driven column validation
- train-test drift detection
- drift report generation
- validated train/test export
- data transformation with `KNNImputer`
- transformed NumPy array export
- preprocessing object export
- logging and exception system

Next likely steps:

- model training
- model evaluation
- prediction pipeline

## Notes

- This project is currently in the early pipeline-building stage.
- The ingestion, validation, and transformation modules are now implemented.
- Some spellings in file and folder names, such as `phisingData.csv` and `trainig_pipeline`, are kept as they exist in the current codebase.
- `pymongo` must be installed in the active Python environment before running `main.py`.

## Author

Om Kulkarni

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:22c55e,50:0ea5e9,100:0f172a&height=120&section=footer" alt="Footer Banner" />
</p>
