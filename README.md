# 🏭 Mock-Manufacturing-Data-Integrator  
*A Python-based ETL pipeline for cleaning and standardizing manufacturing test data.*

---

## 📌 Overview

Real-world manufacturing environments often produce messy, inconsistent, or non-standardized test reports.  
This project simulates an **end-to-end data integration pipeline** that:

- Loads raw Excel test reports from a simulated EMS factory  
- Cleans and normalizes inconsistent column names  
- Parses values with units (e.g., `"5.1V"` → `5.1`)  
- Handles missing values, invalid timestamps, and formatting issues  
- Standardizes test results (e.g., `"OK"/"Pass"` → `"PASS"`)  
- Converts the cleaned rows into JSON records  
- Submits each record to a mock server endpoint using a REST-style client

The goal is to demonstrate practical experience with **Python, Pandas, data cleaning, ETL pipelines, and API interactions**.

---

## 🧱 Features

### ✔ Data Loading
- Reads messy factory reports in `.xlsx` format  
- Supports configurable input path via environment variables

### ✔ Data Cleaning & Transformation
- Drops empty rows and invalid entries  
- Normalizes column names  
- Extracts numeric values from mixed text (e.g., `"4.8V"`) using regex  
- Coerces invalid numeric or timestamp values safely  
- Converts timestamps into ISO 8601 format  
- Standardizes test result labels (`"OK"`, `"Pass"`, `"FAIL"`, etc.)

### ✔ REST-style Upload Client
- Simulates uploading processed test data to a backend system  
- Includes authentication header  
- Handles timeouts, connection errors, and unexpected responses  
- Logs submission results for each record

### ✔ Configuration
- All external parameters can be injected via environment variables:
  - `IOT_RAW_FILE`
  - `WATS_API`

---

## 📂 Project Structure

```text
Mock-Manufacturing-Data-Integrator/
├── data/
│   └── factory_test_report.xlsx   # Sample "dirty" data source
├── src/
│   ├── __init__.py                # Package definition
│   ├── converter.py               # Logic for loading and cleaning data
│   └── mock_pywats.py             # Simulated SDK for API communication
├── .env                           # Environment variables (API Key, URL)
├── .gitignore                     # Git ignore rules (venv, __pycache__, .env)
├── main.py                        # Entry point of the application
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```