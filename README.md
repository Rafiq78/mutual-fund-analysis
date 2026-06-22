# Mutual Fund Analysis Project

## Overview

This project focuses on mutual fund NAV data ingestion, validation, and analysis using Python and live API integration.

## Features

* Live NAV data fetching using mfapi.in API
* CSV data ingestion using Pandas
* Data quality validation
* Missing value and duplicate detection
* Automated dataset processing
* Git and GitHub integration

## Technologies Used

* Python
* Pandas
* NumPy
* Requests
* Matplotlib
* Plotly
* Git & GitHub

## Project Structure

mutual-fund-analysis/
│
├── data/
│   └── raw/
│
├── reports/
│
├── scripts/
│   ├── data_ingestion.py
│   └── live_nav_fetch.py
│
├── requirements.txt
└── .gitignore

## How to Run

1. Clone repository
2. Create virtual environment
3. Install dependencies:

pip install -r requirements.txt

4. Run scripts:

python scripts/live_nav_fetch.py
python scripts/data_ingestion.py

## Data Quality Findings

* No missing values detected
* No duplicate rows detected
* AMFI scheme mapping inconsistencies observed in API responses
