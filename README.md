
# Data Acquisition Pipeline

A modular Python data acquisition pipeline that fetches data from an external API, transforms the raw response into a structured format, performs basic data cleaning, and saves the processed data to disk.

---

## Project Overview

This project demonstrates the fundamental architecture of a data acquisition pipeline.

The system retrieves post data from the JSONPlaceholder API and processes it through multiple independent stages, with each stage responsible for a single task.

Pipeline Flow:

```text
JSONPlaceholder API
        ↓
data_source.py
        ↓
list[dict]
        ↓
data_formatter.py
        ↓
DataFrame
        ↓
data_cleaner.py
        ↓
Clean DataFrame
        ↓
data_saver.py
        ↓
posts.csv
```

The complete workflow is orchestrated through a single entry point:

```text
pipeline_runner.py
```

---

## Features

- Fetch data from an external REST API
- Convert JSON responses into Pandas DataFrames
- Remove missing values
- Remove duplicate records
- Save processed data as CSV
- Modular pipeline architecture
- End-to-end pipeline execution from a single runner script

---

## Project Structure

```text
data-acquisition-pipeline/
│
├── data/
│   ├── raw/
│   ├── processed/
│   │   └── posts.csv
│
├── docs/
│
├── src/
│   ├── data_source.py
│   ├── data_formatter.py
│   ├── data_cleaner.py
│   ├── data_saver.py
│   └── pipeline_runner.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Module Responsibilities

### data_source.py

Responsible for data acquisition.

Input:

- API Endpoint

Output:

- Python list of dictionaries

Example Output:

```python
[
    {
        "userId": 1,
        "id": 1,
        "title": "Sample Title",
        "body": "Sample Body"
    }
]
```

---

### data_formatter.py

Responsible for transforming raw API data into a structured tabular format.

Input:

```python
list[dict]
```

Output:

```python
pandas.DataFrame
```

---

### data_cleaner.py

Responsible for improving data quality.

Operations:

- Remove duplicate rows
- Remove rows containing missing values
- Reset DataFrame index

Output:

```python
Clean DataFrame
```

---

### data_saver.py

Responsible for persisting processed data.

Input:

```python
DataFrame
```

Output:

```text
CSV File
```

Saved Location:

```text
data/processed/posts.csv
```

---

### pipeline_runner.py

Responsible for orchestrating the complete workflow.

Pipeline Steps:

1. Fetch data
2. Format data
3. Clean data
4. Save data

This is the main entry point of the application.

---

## Technologies Used

- Python 3
- Requests
- Pandas

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd data-acquisition-pipeline
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Linux / macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running The Pipeline

Execute:

```bash
python src/pipeline_runner.py
```

Expected Output:

```text
Fetching posts...
Formatting posts...
Cleaning posts...
Saving data...
Pipeline completed successfully
```

---

## Output

After successful execution, the processed dataset is saved as:

```text
data/processed/posts.csv
```

Example:

```csv
userId,id,title,body
1,1,sunt aut facere repellat provident occaecati excepturi optio reprehenderit,...
2,2,qui est esse,...
```

---

## Learning Objectives

This project demonstrates:

- API-based data acquisition
- HTTP requests using Requests
- JSON-to-Python data conversion
- Pandas DataFrame creation
- Basic data cleaning workflows
- CSV persistence
- Modular software architecture
- Pipeline orchestration
- Separation of responsibilities
- Python modules and imports

---

## Key Concepts Practiced

### Data Acquisition

Fetching external data from a REST API.

### Data Formatting

Transforming raw JSON responses into tabular structures.

### Data Cleaning

Removing invalid or incomplete records.

### Data Persistence

Saving processed data to permanent storage.

### Pipeline Orchestration

Coordinating multiple independent modules through a single entry point.

---

## Future Improvements

Potential enhancements include:

- Support for multiple APIs
- Configuration-driven pipelines
- Logging system
- Retry mechanisms for API failures
- Schema validation
- Data quality reports
- Database integration
- Automated testing
- Scheduled execution
- Docker containerization

---

## Project Status

```text
Version: V1
Status: Complete
```

The current version successfully demonstrates a complete end-to-end data acquisition pipeline using a modular architecture.

---

## Author

Anshuman 
