
EXPERIMENT NO. 7

TITLE: BASELINE MODEL DEVELOPMENT AND HYPERPARAMETER TUNING WITH MLFLOW

AIM:
To develop a baseline machine learning model, select hyperparameters, apply Grid Search and Random Search techniques, evaluate model performance, track experiments using MLflow, and compare model results.

DESCRIPTION:
A baseline model provides an initial performance benchmark before applying tuning techniques.

Hyperparameter tuning improves model performance by searching for suitable parameter values.

Grid Search checks all specified parameter combinations, whereas Random Search selects random combinations. MLflow is used to track and compare experiments.

STEP 1: INSTALL REQUIRED LIBRARIES

Open Command Prompt or VS Code Terminal and execute:

pip install scikit-learn mlflow numpy

Check MLflow installation:

mlflow --version

STEP 2: CREATE PROJECT FOLDER

Create a folder named:

Experiment7

Inside the folder, create a Python file:

hyperparameter_tuning.py

STEP 3: COMPLETE PYTHON PROGRAM

# Import required libraries

from sklearn.svm import SVC
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV

import mlflow
import numpy as np

# Load Wine dataset
data = load_wine()

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    data.data,
    data.target,
    test_size=0.25,
    random_state=1
)

# Set MLflow experiment
mlflow.set_experiment("wine-hyperparameter-tuning")


# 1. BASELINE MODEL

with mlflow.start_run(run_name="baseline"):

    baseline = SVC()

    baseline.fit(X_train, y_train)

    acc = accuracy_score(
        y_test,
        baseline.predict(X_test)
    )

    mlflow.log_metric("accuracy", acc)

    print(f"Baseline accuracy: {acc:.3f}")


# 2. GRID SEARCH

param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf'],
    'gamma': ['scale', 'auto']
}

with mlflow.start_run(run_name="grid-search"):

    grid = GridSearchCV(
        SVC(),
        param_grid,
        cv=5,
        scoring='accuracy'
    )

    grid.fit(X_train, y_train)

    acc = accuracy_score(
        y_test,
        grid.best_estimator_.predict(X_test)
    )

    mlflow.log_params(grid.best_params_)

    mlflow.log_metric("accuracy", acc)

    print(f"Grid Search best params: {grid.best_params_}")

    print(f"Grid Search test accuracy: {acc:.3f}")


# 3. RANDOM SEARCH

param_dist = {
    'C': np.logspace(-2, 2, 20),
    'kernel': ['linear', 'rbf', 'poly'],
    'gamma': ['scale', 'auto']
}

with mlflow.start_run(run_name="random-search"):

    rand_search = RandomizedSearchCV(
        SVC(),
        param_dist,
        n_iter=15,
        cv=5,
        random_state=42
    )

    rand_search.fit(X_train, y_train)

    acc = accuracy_score(
        y_test,
        rand_search.best_estimator_.predict(X_test)
    )

    mlflow.log_params(rand_search.best_params_)

    mlflow.log_metric("accuracy", acc)

    print(f"Random Search best params: {rand_search.best_params_}")

    print(f"Random Search test accuracy: {acc:.3f}")


STEP 4: EXECUTION

Save the Python file and execute:

python hyperparameter_tuning.py

STEP 5: EXPECTED OUTPUT

The manual provides the following example output:

Baseline accuracy: 0.711

Grid Search best params:
{'C': 10, 'gamma': 'scale', 'kernel': 'linear'}

Grid Search test accuracy: 0.978

Random Search best params:
{'kernel': 'linear', 'gamma': 'auto', 'C': 18.32}

Random Search test accuracy: 0.978

NOTE:
Actual results may vary depending on library versions and execution environment. Random Search may also select a different combination.

STEP 6: EXPERIMENT TRACKING USING MLFLOW

MLflow tracks the performance of all three approaches:

1. Baseline Model
2. Grid Search
3. Random Search

The following information is recorded:

- Model parameters
- Accuracy score
- Experiment name
- Run name

STEP 7: VIEW RESULTS USING MLFLOW UI

Open another terminal in the same project folder.

Execute:

mlflow ui

Open the following URL in your browser:

http://127.0.0.1:5000

Select the experiment:

wine-hyperparameter-tuning

Compare the results of all three runs.

STEP 8: COMPARATIVE ANALYSIS

Approach          Best Parameters                  Test Accuracy

Baseline          Default SVC()                    0.711

Grid Search       C=10, kernel=linear,             0.978
                  gamma=scale

Random Search     C=18.32, kernel=linear,          0.978
                  gamma=auto

STEP 9: ANALYSIS

1. The baseline model provides an initial accuracy of 0.711.
2. Grid Search improves accuracy to 0.978.
3. Random Search also improves accuracy to 0.978.
4. Both tuning techniques perform better than the baseline model.
5. Grid Search checks every specified combination, while Random Search explores selected random combinations.
6. MLflow helps track and compare all experiments.

STEP 10: CONCLUSION

Thus, we have developed a baseline machine learning model, tuned its hyperparameters using Grid Search and Random Search, tracked experiments using MLflow, and performed comparative analysis to identify the best-performing configuration.

VIVA QUESTIONS AND ANSWERS

1. What is a baseline model?
A baseline model is an initial machine learning model used as a reference for comparing improved models.

2. What is hyperparameter tuning?
It is the process of selecting suitable hyperparameter values to improve model performance.

3. What is Grid Search?
Grid Search tests all possible combinations of specified hyperparameter values.

4. What is Random Search?
Random Search selects and tests a fixed number of random hyperparameter combinations.

5. What is SVC?
SVC stands for Support Vector Classifier. It is a supervised machine learning algorithm used for classification.

6. What is MLflow?
MLflow is an open-source platform used for tracking and managing machine learning experiments.

7. What is accuracy?
Accuracy is the ratio of correctly predicted observations to the total observations.

8. What is the Wine dataset?
The Wine dataset is a classification dataset containing chemical measurements of wines from three different classes.

9. What is GridSearchCV?
GridSearchCV performs an exhaustive search over specified hyperparameter combinations using cross-validation.

10. What is RandomizedSearchCV?
RandomizedSearchCV tests a fixed number of randomly selected hyperparameter combinations.

11. Which is more computationally expensive?
Grid Search can be more computationally expensive because it evaluates every specified combination.

12. Why do we use MLflow?
MLflow helps record, track and compare different machine learning experiments.
