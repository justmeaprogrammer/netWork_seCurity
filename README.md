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
  <img src="https://img.shields.io/badge/Current%20Module-Data%20Ingestion-16A34A?style=flat-square" alt="Current Module" />
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
- MongoDB upload utility added
- train/test data export flow connected through `main.py`

## Snapshot

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=OmKulkarni&show_icons=true&hide_border=true&title_color=0f172a&icon_color=0ea5e9&text_color=334155&bg_color=ffffff" alt="GitHub Stats" />
</p>

If the stats card does not load on GitHub, the rest of the README still works normally.

## Project Flow

The current flow of the project is:

1. Read phishing data from `Network_data/phisingData.csv`
2. Upload records into MongoDB using `push_data.py`
3. Start the ingestion pipeline from `main.py`
4. Read the collection from MongoDB into a pandas DataFrame
5. Save the full dataset into the feature store
6. Split the data into train and test sets
7. Save the generated files inside the `Artifacts/` directory

## Project Structure

```text
NetworkSecurity/
├── Network_data/
│   └── phisingData.csv
├── networksecurity/
│   ├── components/
│   │   └── data_ingestion.py
│   ├── constant/
│   │   └── trainig_pipeline/
│   │       └── __init__.py
│   ├── entity/
│   │   ├── artifact_entity.py
│   │   └── config_entity.py
│   ├── exception/
│   │   └── exception.py
│   └── logging/
│       └── logger.py
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

### `networksecurity/entity/config_entity.py`

This file contains config classes:

- `TrainingPipelineConfig`
- `DataIngestionConfig`

These classes prepare folder paths, file paths, database names, and split settings.

### `networksecurity/entity/artifact_entity.py`

This file contains `DataIngestionArtifact`, which stores the output paths of generated train and test files.

### `networksecurity/constant/trainig_pipeline/__init__.py`

This file stores project constants such as:

- artifact folder names
- file names
- MongoDB collection name
- MongoDB database name
- train-test split ratio

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

### 4. Run the ingestion pipeline

```bash
python main.py
```

## Output

After running the pipeline, the project creates:

- feature-store CSV file
- train CSV file
- test CSV file
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
```

## What Is Implemented So Far

Completed:

- ingestion pipeline skeleton
- MongoDB connection flow
- feature store export
- train-test split export
- logging and exception system

Next likely steps:

- data validation
- data transformation
- model training
- model evaluation
- prediction pipeline

## Notes

- This project is currently in the early pipeline-building stage.
- The main implemented module right now is data ingestion.
- Some spellings in file and folder names, such as `phisingData.csv` and `trainig_pipeline`, are kept as they exist in the current codebase.

## Author

Om Kulkarni

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:22c55e,50:0ea5e9,100:0f172a&height=120&section=footer" alt="Footer Banner" />
</p>
