# azure-data-pipeline-samples


# Azure Data Pipeline Samples

## Overview

This project demonstrates a simplified Azure Data Factory (ADF) style ETL pipeline built using Python and JSON datasets.

The goal is to simulate a real-world enterprise data engineering workflow where customer and order data are ingested, validated, transformed, and exported for reporting.

---

## Technologies

- Python 3
- Pandas
- JSON
- Azure Data Factory (Sample Configuration)
- Git

---

## Project Structure

```
azure-data-pipeline-samples
│
├── data
│   ├── customers.json
│   ├── orders.json
│   └── output.csv
│
├── python
│   ├── merge_data.py
│   ├── validate_data.py
│
├── adf
│   └── pipeline.json
│
├── docs
│   └── architecture.md
│
└── README.md
```

---

## Workflow

1. Read customer data
2. Read order data
3. Merge datasets
4. Validate records
5. Export CSV
6. Ready for reporting

---

## Features

✔ JSON Data Ingestion

✔ Data Transformation

✔ Data Validation

✔ CSV Export

✔ Sample Azure Data Factory Pipeline

✔ Unit Tests

---

## Future Improvements

- Azure Blob Storage Integration
- Azure SQL Database
- Azure Data Factory Deployment
- Automated Scheduling
- Docker Support
