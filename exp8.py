EXPERIMENT NO. 8
TITLE: UNIT TESTING OF ML PIPELINE

AIM:
To perform unit testing of data processing functions, testing of
training pipelines, validation of model outputs, creation of
automated test cases, execution of tests using CI tools, and
analysis of test results.

--------------------------------------------------
STEP 1: INSTALL REQUIRED LIBRARIES
--------------------------------------------------

Open VS Code terminal and execute:

pip install pandas numpy scikit-learn pytest

Check pytest installation:

pytest --version


--------------------------------------------------
STEP 2: CREATE PROJECT FOLDER
--------------------------------------------------

Create a folder named Experiment8.

Inside it, create two Python files:

Experiment8/
    |
    |--- pipeline.py
    |
    |--- test_pipeline.py


--------------------------------------------------
STEP 3: CREATE pipeline.py
(CODE UNDER TEST)
--------------------------------------------------

import pandas as pd

# Function to remove null values
def remove_nulls(df):
    return df.dropna()

# Function to normalize data
def normalize(df, column):
    df[column] = (df[column] - df[column].mean()) / df[column].std()
    return df

# Function to train the ML model
def train_model(X, y):
    from sklearn.linear_model import LogisticRegression

    model = LogisticRegression(max_iter=200)
    model.fit(X, y)

    return model


--------------------------------------------------
STEP 4: CREATE test_pipeline.py
(UNIT TEST CASES)
--------------------------------------------------

import pandas as pd
import numpy as np

from pipeline import remove_nulls, normalize, train_model


# TEST 1: Testing null value removal
def test_remove_nulls():
    df = pd.DataFrame({'a': [1, None, 3]})

    result = remove_nulls(df)

    assert result.isnull().sum().sum() == 0
    assert len(result) == 2


# TEST 2: Testing data normalization
def test_normalize():
    df = pd.DataFrame({'a': [10, 20, 30]})

    result = normalize(df, 'a')

    assert abs(result['a'].mean()) < 1e-6
    assert abs(result['a'].std() - 1.0) < 1e-6


# TEST 3: Testing model output shape
def test_train_model_output_shape():
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y = np.array([0, 0, 1, 1])

    model = train_model(X, y)
    preds = model.predict(X)

    assert preds.shape == y.shape
    assert set(preds).issubset({0, 1})


# TEST 4: Testing model prediction accuracy
def test_model_predicts_reasonably():
    X = np.array([[1, 1], [1, 2], [10, 10], [10, 11]])
    y = np.array([0, 0, 1, 1])

    model = train_model(X, y)

    accuracy = model.score(X, y)

    assert accuracy >= 0.75


--------------------------------------------------
STEP 5: EXECUTE THE TEST CASES
--------------------------------------------------

Open the terminal inside the Experiment8 folder.

Execute:

pytest test_pipeline.py -v


--------------------------------------------------
STEP 6: EXPECTED OUTPUT
--------------------------------------------------

test_pipeline.py::test_remove_nulls PASSED

test_pipeline.py::test_normalize PASSED

test_pipeline.py::test_train_model_output_shape PASSED

test_pipeline.py::test_model_predicts_reasonably PASSED

==============================
4 passed in 0.42s
==============================


--------------------------------------------------
STEP 7: EXECUTION USING CI TOOLS
--------------------------------------------------

The same test suite can be executed automatically on every
push using a CI tool such as GitHub Actions.

Operations:

1. Push the project code to GitHub.
2. GitHub Actions starts the CI workflow.
3. The required dependencies are installed.
4. Pytest executes the test cases.
5. The test results are displayed.
6. The developer checks whether all tests passed.


--------------------------------------------------
STEP 8: FREQUENTLY USED PYTEST COMMANDS
--------------------------------------------------

Check pytest version:

pytest --version

Run all tests in the current directory:

pytest

Run tests in verbose mode:

pytest -v

Run tests matching a keyword:

pytest -k "normalize"

List tests without executing them:

pytest --collect-only


--------------------------------------------------
STEP 9: ANALYSIS OF TEST RESULTS
--------------------------------------------------

1. All four test cases passed successfully.
2. Null value handling was tested.
3. Data normalization was verified.
4. Model output shape was validated.
5. Model prediction accuracy was checked.
6. Unit testing helps detect errors early.
7. Tests can be executed automatically using CI tools.


--------------------------------------------------
STEP 10: CONCLUSION
--------------------------------------------------

Thus, we successfully performed unit testing of data
processing functions and the machine learning training
pipeline using Python's pytest framework.

We validated model outputs, executed automated test cases,
and analysed the test results to confirm the correctness
of the ML pipeline.


--------------------------------------------------
IMPORTANT VIVA QUESTIONS AND ANSWERS
--------------------------------------------------

1. What is unit testing?
   Testing individual functions or components separately.

2. Which framework is used in this experiment?
   Pytest.

3. What is pytest?
   Pytest is a Python framework used for automated testing.

4. What is assert?
   Assert checks whether a condition is true.

5. What is a DataFrame?
   A two-dimensional data structure provided by Pandas.

6. What does dropna() do?
   It removes rows containing missing values.

7. What is normalization?
   Scaling data to a common scale.

8. What is Logistic Regression?
   A supervised machine learning classification algorithm.

9. What does fit() do?
   It trains the machine learning model.

10. What does predict() do?
    It predicts output for given input data.

11. What does model.score() return?
    It returns the model's accuracy score for this classifier.

12. What does -v mean in pytest?
    It enables verbose output.

13. How many test cases are used?
    Four test cases.

14. What is CI?
    Continuous Integration.

15. Why is testing important in MLOps?
    It helps ensure that data processing and model code
    work correctly.
