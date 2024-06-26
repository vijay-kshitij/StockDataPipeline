# StockDataPipeline

In this project, we aim to build a comprehensive pipeline that extracts historical stock data from yfinance, processes the data using Python, and deploys the code on Apache Airflow running on an EC2 instance provided by Amazon Web Services (AWS). Finally, the processed data will be stored in Amazon S3. 

### Technologies Used
- Python
- yfinance
- Apache Airflow
- AWS S3
- AWS EC2

### Project Files
- data_extraction.py: Extracts historical stock data and saves it as a CSV file.
- dag_file.py: Defines an Airflow DAG that automates the upload of the CSV file to AWS S3.
