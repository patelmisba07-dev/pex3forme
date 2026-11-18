
EXPERIMENT NO. 9

TITLE: SETTING UP A CONTINUOUS INTEGRATION PIPELINE USING GITHUB ACTIONS

AIM:
To set up GitHub Actions or GitLab CI, automate the build process, create an automated testing workflow, validate model training scripts, generate build reports and document the Continuous Integration pipeline.

DESCRIPTION:
Continuous Integration (CI) automatically builds, tests and validates code whenever changes are pushed to a repository.

In MLOps, a CI pipeline installs dependencies, runs unit tests on data-processing and training scripts, and generates reports to identify errors before deployment.

STEP 1: CREATE A GITHUB REPOSITORY

1. Open https://github.com
2. Sign in to your account.
3. Click New Repository.
4. Enter the repository name:

   MLOps-CI-Experiment

5. Select Public or Private.
6. Click Create Repository.

STEP 2: CREATE PROJECT STRUCTURE

Create the following files in your project:

MLOps-CI-Experiment/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
├── pipeline.py
├── test_pipeline.py
└── train.py

NOTE:
The pipeline.py and test_pipeline.py files contain the data-processing functions and unit tests from Experiment 8.

STEP 3: CREATE REQUIREMENTS.TXT

Add the following dependencies:

pandas
numpy
scikit-learn
pytest
pytest-html

STEP 4: CREATE PIPELINE.PY

import pandas as pd

def remove_nulls(df):
    return df.dropna()

def normalize(df, column):
    df[column] = (
        df[column] - df[column].mean()
    ) / df[column].std()

    return df

def train_model(X, y):
    from sklearn.linear_model import LogisticRegression

    model = LogisticRegression(max_iter=200)
    model.fit(X, y)

    return model

STEP 5: CREATE TEST_PIPELINE.PY

import pandas as pd
import numpy as np

from pipeline import remove_nulls, normalize, train_model

def test_remove_nulls():

    df = pd.DataFrame({'a': [1, None, 3]})

    result = remove_nulls(df)

    assert result.isnull().sum().sum() == 0
    assert len(result) == 2


def test_normalize():

    df = pd.DataFrame({'a': [10, 20, 30]})

    result = normalize(df, 'a')

    assert abs(result['a'].mean()) < 1e-6
    assert abs(result['a'].std() - 1.0) < 1e-6


def test_train_model_output_shape():

    X = np.array([
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5]
    ])

    y = np.array([0, 0, 1, 1])

    model = train_model(X, y)

    preds = model.predict(X)

    assert preds.shape == y.shape
    assert set(preds).issubset({0, 1})


def test_model_predicts_reasonably():

    X = np.array([
        [1, 1],
        [1, 2],
        [10, 10],
        [10, 11]
    ])

    y = np.array([0, 0, 1, 1])

    model = train_model(X, y)

    accuracy = model.score(X, y)

    assert accuracy >= 0.75

STEP 6: CREATE TRAIN.PY

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    '--quick-check',
    action='store_true'
)

args = parser.parse_args()

if args.quick_check:

    print("Running a 1-epoch sanity check on a small data sample...")

    print("Sanity check completed successfully.")

else:

    print("Running full training...")

NOTE:
This is a simple execution-check example based on the manual's training-script excerpt. For actual model training, the quick-check section must be connected to your training code.

STEP 7: CREATE GITHUB ACTIONS WORKFLOW

Create the following folder structure:

.github/workflows/

Inside it, create a file named:

ci.yml

Add the following code:

name: ML Pipeline CI

on:
  push:
    branches: [ main ]

  pull_request:
    branches: [ main ]

jobs:
  build-and-test:

    runs-on: ubuntu-latest

    steps:

      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-html

      - name: Run unit tests
        run: pytest test_pipeline.py --html=report.html --self-contained-html

      - name: Validate training script executes
        run: python train.py --quick-check

      - name: Upload test report
        uses: actions/upload-artifact@v4
        with:
          name: test-report
          path: report.html

STEP 8: PUSH PROJECT TO GITHUB

Open the terminal in your project folder and execute:

git init

git add .

git commit -m "Add MLOps CI pipeline"

git branch -M main

git remote add origin YOUR_GITHUB_REPOSITORY_URL

git push -u origin main

Replace YOUR_GITHUB_REPOSITORY_URL with your actual GitHub repository URL.

STEP 9: AUTOMATED BUILD PROCESS

Whenever code is pushed to the main branch:

1. GitHub Actions starts an Ubuntu runner.
2. It checks out the latest repository code.
3. It installs Python 3.10.
4. It installs the required dependencies.
5. It executes the automated tests.
6. It validates the training script.
7. It uploads the HTML test report.

STEP 10: AUTOMATED TESTING WORKFLOW

The following command executes all unit tests:

pytest test_pipeline.py --html=report.html --self-contained-html

This command:

- Runs the test cases using pytest.
- Checks data-processing functions.
- Validates model outputs.
- Generates an HTML test report.

STEP 11: VALIDATION OF MODEL TRAINING SCRIPT

Execute:

python train.py --quick-check

Expected output:

Running a 1-epoch sanity check on a small data sample...

Sanity check completed successfully.

STEP 12: GENERATION OF BUILD REPORTS

The test report is generated using:

pytest test_pipeline.py --html=report.html --self-contained-html

Expected example output:

==================== 4 passed in 0.55s ====================

Generated html report: report.html

The report can be downloaded from the Artifacts section of the successful GitHub Actions workflow run.

STEP 13: VERIFY GITHUB ACTIONS

1. Open your GitHub repository.
2. Click the Actions tab.
3. Select ML Pipeline CI.
4. Open the latest workflow run.
5. Check whether all steps are successful.
6. Download the test-report artifact.

STEP 14: CI PIPELINE DOCUMENTATION

Stage             Action                         Failure Response

Checkout          Pull latest code               Pipeline stops immediately

Setup             Install Python and dependencies Pipeline fails

Test              Run pytest and generate report  Failed tests are listed

Validate          Execute training script         Pipeline fails if script errors

Artifact Upload   Publish test report             Runs if previous steps pass

STEP 15: BASIC / FREQUENTLY USED GITHUB CLI COMMANDS

gh --version
# Check GitHub CLI version

gh auth login
# Authenticate with GitHub

gh repo view
# View repository details

gh workflow list
# List CI workflows

gh run list
# List recent workflow runs

CONCLUSION:

Thus, we have set up a Continuous Integration pipeline using GitHub Actions that automatically builds the project, runs automated tests, validates the model training script and generates a downloadable build/test report on every code change.

VIVA QUESTIONS AND ANSWERS

1. What is Continuous Integration?
CI is a software development practice that automatically builds and tests code whenever changes are made.

2. What is GitHub Actions?
GitHub Actions is a CI/CD platform used to automate workflows directly in GitHub repositories.

3. What is a CI pipeline?
A CI pipeline is a sequence of automated steps used to build, test and validate code.

4. What is a workflow?
A workflow is an automated process defined in a YAML file.

5. What is a YAML file?
YAML is a human-readable format used for configuration files.

6. What is pytest?
Pytest is a Python framework used for writing and executing automated tests.

7. What is requirements.txt?
It is a file that contains the Python dependencies required by a project.

8. What is an Ubuntu runner?
It is a virtual environment provided by GitHub Actions to execute workflow jobs.

9. What is an artifact?
An artifact is a file generated during workflow execution, such as an HTML test report.

10. What is the purpose of automated testing?
It helps identify errors automatically and ensures that code works correctly.

11. What is the purpose of ci.yml?
It defines the GitHub Actions workflow and its automated steps.

12. What is the difference between CI and CD?
CI focuses on automatically building and testing code, whereas CD focuses on delivering or deploying validated changes.
