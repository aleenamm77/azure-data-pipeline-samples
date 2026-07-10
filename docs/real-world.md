# Real World ETL Workflow

This sample project mimics a common enterprise ETL pipeline.

## Extract

Customer and order data are collected from source systems.

Examples:

- CRM
- ERP
- REST APIs
- Azure Blob Storage

---

## Transform

The datasets are merged and cleaned.

Typical transformations include

- Remove duplicates
- Handle null values
- Rename columns
- Standardize formats

---

## Load

The processed data can be loaded into

- Azure SQL Database
- Azure Synapse Analytics
- Data Warehouse
- Power BI

---

## Validation

Before loading, quality checks verify

- Missing values
- Duplicate records
- Invalid data types

This repository demonstrates the same concepts using Python scripts and sample JSON files.
