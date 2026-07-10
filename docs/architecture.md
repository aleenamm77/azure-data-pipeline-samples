# Azure Data Pipeline Architecture
                +------------------+
                | customers.json   |
                +------------------+
                          |
                          |
                +------------------+
                |  Azure Data      |
                | Factory Pipeline |
                +------------------+
                          |
          +---------------+---------------+
          |                               |
          |                               |
+--------------------+        +--------------------+
| Data Validation    |        | Data Transformation|
| (Python Script)    |        | (Merge Script)     |
+--------------------+        +--------------------+
          |                               |
          +---------------+---------------+
                          |
                 +------------------+
                 | output.csv       |
                 +------------------+
                          |
                 Business Reporting
