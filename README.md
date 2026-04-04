# Network Security

A beginner-friendly machine learning project for phishing data ingestion and pipeline setup.

This repository currently focuses on the first core stage of the project:

- loading phishing data from a CSV file
- pushing that data into MongoDB
- reading the data back from MongoDB
- saving a feature-store copy
- splitting the dataset into train and test files

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
