



# Engineering Log — Data Acquisition Pipeline

## Project Information

**Project Name:** Data Acquisition Pipeline

**Status:** Completed (V1)

**Objective:**

Build a modular data acquisition pipeline capable of:

- Fetching data from an external API
- Formatting raw JSON data
- Cleaning data
- Saving processed output
- Executing the entire workflow through a single orchestrator

---

## Architecture

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

---

## Development Timeline

### Project Setup

**Tasks Completed**

- Created GitHub repository
- Created project folder structure
- Created virtual environment
- Installed dependencies
- Generated requirements.txt
- Configured .gitignore

**Dependencies**

- requests
- pandas

---

## Module Development

### 1. data_source.py

#### Purpose

Fetch data from an external API.

#### Implementation

- Used Requests library
- Sent HTTP GET request
- Retrieved JSON response
- Converted response into Python objects

#### Input

```text
API Endpoint
```

#### Output

```python
list[dict]
```

#### Validation

- Successfully connected to API
- Retrieved 100 records
- Verified JSON structure

---

### 2. data_formatter.py

#### Purpose

Convert raw API response into a structured tabular format.

#### Implementation

```python
pd.DataFrame(posts)
```

#### Input

```python
list[dict]
```

#### Output

```python
pandas.DataFrame
```

#### Validation

- Verified DataFrame creation
- Verified columns generated from dictionary keys
- Verified rows generated from records

---

### 3. data_cleaner.py

#### Purpose

Perform basic data quality operations.

#### Implementation

```python
drop_duplicates()
dropna()
reset_index(drop=True)
```

#### Input

```python
DataFrame
```

#### Output

```python
Clean DataFrame
```

#### Validation

- Tested duplicate removal
- Tested missing value removal
- Tested index reset

---

### 4. data_saver.py

#### Purpose

Persist processed data.

#### Implementation

```python
df.to_csv()
```

#### Input

```python
DataFrame
```

#### Output

```text
CSV File
```

#### Validation

- Confirmed CSV generation
- Verified output file contents
- Verified output file location

---

### 5. pipeline_runner.py

#### Purpose

Orchestrate the complete pipeline.

#### Workflow

```text
Fetch Data
    ↓
Format Data
    ↓
Clean Data
    ↓
Save Data
```

#### Validation

Successfully executed the complete pipeline from a single entry point.

Expected Output:

```text
Fetching posts...
Formatting posts...
Cleaning posts...
Saving data...
Pipeline completed successfully.
```

---

## Challenges Encountered

### Missing Requests Dependency

#### Issue

```text
ModuleNotFoundError: No module named 'requests'
```

#### Cause

Requests package was not installed in the active virtual environment.

#### Resolution

```bash
pip install requests
```

Updated:

```text
requirements.txt
```

---

### Understanding Python Module Execution

#### Topic

```python
if __name__ == "__main__":
```

#### Areas Explored

- Module imports
- Execution flow
- Function definitions
- Function calls
- Python module structure
- Module testing patterns

#### Outcome

Developed a clear understanding of how Python distinguishes between:

```text
Direct execution
```

and

```text
Module import
```

---

## Final Deliverables

### Source Code

- data_source.py
- data_formatter.py
- data_cleaner.py
- data_saver.py
- pipeline_runner.py

### Documentation

- README.md
- engineering_log.md

### Output

- posts.csv

---

## Project Outcome

Successfully built a complete end-to-end data acquisition pipeline demonstrating:

- API integration
- JSON processing
- DataFrame creation
- Data cleaning
- CSV persistence
- Modular architecture
- Pipeline orchestration
- Separation of responsibilities

---

## Future Improvements

Potential enhancements:

- Multiple API sources
- Retry mechanisms
- Logging
- Schema validation
- Configuration files
- Database integration
- Automated testing
- Dockerization
- Scheduled execution

---

## Project Status

```text
Version: V1
Status: Complete
```

