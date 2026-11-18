
EXPERIMENT NO. 4
TITLE: DESIGN AND AUTOMATION OF AN END-TO-END DATA PIPELINE

AIM:
To perform data collection, data preprocessing, feature engineering,
data validation, pipeline design, automation of data processing
workflow, execution of an end-to-end data pipeline, and documentation
of pipeline stages.

--------------------------------------------------
DESCRIPTION:
--------------------------------------------------

A data pipeline automates the flow of data from raw sources through
cleaning, transformation and validation, so that consistent,
high-quality data is available for model training.

This experiment builds a simple end-to-end data pipeline covering
data collection, preprocessing, feature engineering and validation.

--------------------------------------------------
STEP 1: INSTALL REQUIRED LIBRARIES
--------------------------------------------------

Open VS Code terminal and execute:

pip install pandas scikit-learn

--------------------------------------------------
STEP 2: CREATE PROJECT FOLDER
--------------------------------------------------

Create a folder named:

ML_Pipeline

Inside it, create these files:

ML_Pipeline/
    |
    |--- raw_data.csv
    |
    |--- pipeline.py
    |
    |--- run_pipeline.sh

--------------------------------------------------
STEP 3: CREATE raw_data.csv
(SAMPLE INPUT DATA)
--------------------------------------------------

Create a file named raw_data.csv.

Enter the following data:

name,age,income
A,20,20000
B,25,30000
C,30,40000
D,35,50000
E,40,60000
F,25,35000
G,30,45000
H,45,70000
I,50,80000
J,55,90000

Save the file.

--------------------------------------------------
STEP 4: CREATE pipeline.py
(END-TO-END DATA PIPELINE)
--------------------------------------------------

import pandas as pd
from sklearn.preprocessing import StandardScaler

# Step 1: Data Collection
def collect_data(path):
    return pd.read_csv(path)


# Step 2: Data Preprocessing
def preprocess(df):
    df = df.drop_duplicates()
    df = df.fillna(df.mean(numeric_only=True))
    return df


# Step 3: Feature Engineering
def engineer_features(df):
    df['income_per_age'] = df['income'] / (df['age'] + 1)

    scaler = StandardScaler()

    df[['age', 'income']] = scaler.fit_transform(
        df[['age', 'income']]
    )

    return df


# Step 4: Data Validation
def validate(df):
    assert df.isnull().sum().sum() == 0, \
        "Validation failed: missing values present"

    assert df['age'].between(-5, 5).all(), \
        "Validation failed: age out of expected range"

    print("Data validation passed.")

    return True


# Step 5: Run Complete Pipeline
def run_pipeline(path):

    df = collect_data(path)
    print(f"Collected {len(df)} records")

    df = preprocess(df)

    df = engineer_features(df)

    validate(df)

    df.to_csv('processed_data.csv', index=False)

    print("Pipeline executed successfully. Output saved to processed_data.csv")


if __name__ == "__main__":
    run_pipeline("raw_data.csv")


--------------------------------------------------
STEP 5: EXECUTE THE PYTHON PROGRAM
--------------------------------------------------

Open the terminal inside the ML_Pipeline folder.

Execute:

python pipeline.py

Expected output for the sample CSV:

Collected 10 records
Data validation passed.
Pipeline executed successfully. Output saved to processed_data.csv

NOTE:
The manual shows an example output of 1000 records.
The actual number depends on the input CSV file.

--------------------------------------------------
STEP 6: CHECK THE OUTPUT FILE
--------------------------------------------------

After successful execution, a new file is created:

processed_data.csv

Open this file.

It contains:
1. Cleaned data.
2. No duplicate records.
3. Missing numeric values filled with mean values.
4. A new feature named income_per_age.
5. Standardized age and income values.

--------------------------------------------------
STEP 7: AUTOMATION OF DATA PROCESSING WORKFLOW
--------------------------------------------------

Create a file named run_pipeline.sh.

Write the following code:

#!/bin/bash

# Automates the daily data pipeline run

echo "Starting data pipeline run: $(date)"

python3 pipeline.py

echo "Pipeline run completed: $(date)"


--------------------------------------------------
STEP 8: EXECUTE THE AUTOMATION SCRIPT
--------------------------------------------------

On Linux or Git Bash, execute:

bash run_pipeline.sh

The script automatically executes pipeline.py.

Expected output:

Starting data pipeline run: [current date and time]

Collected 10 records

Data validation passed.

Pipeline executed successfully. Output saved to processed_data.csv

Pipeline run completed: [current date and time]


--------------------------------------------------
STEP 9: SCHEDULE AUTOMATIC EXECUTION USING CRON
--------------------------------------------------

Open the cron editor:

crontab -e

Add the following entry to run the pipeline every day at 2 AM:

0 2 * * * /home/user/ml-project/run_pipeline.sh >> pipeline.log 2>&1

Save the file.

NOTE:
Replace the example path with the actual path of your script.
Cron is generally used on Linux systems.

The pipeline can also be automated using an orchestrator
such as Apache Airflow.


--------------------------------------------------
STEP 10: ANALYSIS OF RESULTS
--------------------------------------------------

1. Raw data was collected from a CSV file.
2. Duplicate records were removed.
3. Missing numeric values were filled using mean values.
4. A new feature income_per_age was created.
5. Age and income were standardized using StandardScaler.
6. Data validation was performed.
7. Processed data was saved in processed_data.csv.
8. The pipeline was automated using a shell script.

--------------------------------------------------
STEP 11: CONCLUSION
--------------------------------------------------

Thus, we successfully designed and executed an end-to-end
data pipeline covering data collection, preprocessing,
feature engineering and validation.

We also automated the workflow so that it can run repeatedly
without manual intervention.

--------------------------------------------------
IMPORTANT VIVA QUESTIONS AND ANSWERS
--------------------------------------------------

1. What is a data pipeline?
   A data pipeline is a process that collects, transforms
   and validates data.

2. What is the main aim of this experiment?
   To design and automate an end-to-end data pipeline.

3. Which libraries are used?
   Pandas and Scikit-learn.

4. What is data collection?
   It is the process of collecting raw data from different
   sources such as CSV files, databases and APIs.

5. What is data preprocessing?
   It is the process of cleaning and preparing raw data.

6. What is feature engineering?
   It is the process of creating new features from existing data.

7. What is data validation?
   It checks whether data meets the required quality conditions.

8. What does pd.read_csv() do?
   It reads data from a CSV file.

9. What does drop_duplicates() do?
   It removes duplicate records.

10. What does fillna() do?
    It fills missing values in a dataset.

11. What is StandardScaler?
    It standardizes data using mean and standard deviation.

12. What does fit_transform() do?
    It learns scaling parameters from data and transforms it.

13. What is an assert statement?
    It checks whether a condition is true. If false,
    it raises an AssertionError.

14. What is a pipeline?
    It is a sequence of connected data processing stages.

15. What is automation?
    It is the process of executing tasks automatically
    without repeated manual intervention.

16. What is a shell script?
    It is a file containing commands that execute together.

17. What is cron?
    Cron is a Linux utility used to schedule tasks.

18. What is Apache Airflow?
    It is a workflow orchestration tool used to schedule
    and manage data pipelines.

19. What is the output file of this experiment?
    processed_data.csv.

20. What are the main stages of this pipeline?
    Data collection, preprocessing, feature engineering,
    data validation and pipeline automation.
