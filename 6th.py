
EXPERIMENT NO. 6

TITLE: INSTALLATION AND CONFIGURATION OF MLFLOW FOR EXPERIMENT TRACKING

AIM:
To install and configure MLflow, train machine learning models, log parameters and metrics, track artifacts, compare experiments, register models, and select the best model based on experimental results.

DESCRIPTION:
MLflow is an open-source platform used to manage the machine learning lifecycle. It helps track experiments, log parameters, metrics and artifacts, compare model performance, and register trained models.

STEP 1: INSTALLATION AND CONFIGURATION

Open Command Prompt or VS Code Terminal and execute:

pip install mlflow scikit-learn

Check the MLflow version:

mlflow --version

MLflow UI can be started using:

mlflow ui

It starts the tracking interface at:
http://127.0.0.1:5000

STEP 2: CREATE PROJECT FOLDER

Create a folder named:

Experiment6

Inside this folder, create a Python file:

mlflow_experiment.py

STEP 3: COMPLETE PYTHON PROGRAM

import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.datasets import load_iris

# Configure MLflow tracking database
mlflow.set_tracking_uri("sqlite:///mlflow.db")

# Load Iris dataset
data = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    data.data,
    data.target,
    test_size=0.2,
    random_state=42
)

# Set experiment name
mlflow.set_experiment("iris-classification")

best_run_id = None

# Train models with different parameters
for n_estimators in [50, 100, 150]:

    with mlflow.start_run(run_name=f"rf-{n_estimators}"):

        model = RandomForestClassifier(
            n_estimators=n_estimators,
            random_state=42
        )

        model.fit(X_train, y_train)

        preds = model.predict(X_test)

        acc = accuracy_score(y_test, preds)

        f1 = f1_score(
            y_test,
            preds,
            average="macro"
        )

        # Log parameters and metrics
        mlflow.log_param("n_estimators", n_estimators)

        mlflow.log_metric("accuracy", acc)

        mlflow.log_metric("f1_score", f1)

        # Log trained model as an artifact
        mlflow.sklearn.log_model(model, "model")

        print(
            f"n_estimators={n_estimators}, "
            f"accuracy={acc:.3f}, f1={f1:.3f}"
        )

        # Store run ID for the 100-estimator model
        if n_estimators == 100:
            best_run_id = mlflow.active_run().info.run_id

# Register the selected model
result = mlflow.register_model(
    model_uri=f"runs:/{best_run_id}/model",
    name="iris-rf-classifier"
)

print(f"Registered model version: {result.version}")

# Load the registered run's model artifact
loaded_model = mlflow.sklearn.load_model(
    f"runs:/{best_run_id}/model"
)

print("Sample predictions:", loaded_model.predict(X_test[:5]))


STEP 4: EXECUTION

Save the Python file and run:

python mlflow_experiment.py

STEP 5: EXPECTED OUTPUT

The manual shows the following example output:

n_estimators=50, accuracy=0.933, f1=0.932

n_estimators=100, accuracy=0.967, f1=0.966

n_estimators=150, accuracy=0.967, f1=0.966

Registered model version: 1

Sample predictions: [Your model's predicted class values]

NOTE:
The accuracy values may differ because the result depends on the train-test split and environment. The manual's printed values are example results.

STEP 6: ARTIFACT TRACKING

MLflow stores the trained model and its supporting files as artifacts under each experiment run.

To load a model using its run ID:

loaded_model = mlflow.sklearn.load_model(
    "runs:/<RUN_ID>/model"
)

print(loaded_model.predict(X_test[:5]))

Replace <RUN_ID> with the actual run ID.

STEP 7: EXPERIMENT COMPARISON

Open the MLflow UI:

http://127.0.0.1:5000

Select the experiment:

iris-classification

Compare the three runs:

Run       n_estimators    Accuracy    F1 Score
rf-50          50          0.933       0.932
rf-100        100          0.967       0.966
rf-150        150          0.967       0.966

STEP 8: MODEL REGISTRATION

The best model is registered using:

result = mlflow.register_model(
    model_uri="runs:/<RUN_ID_OF_RF_100>/model",
    name="iris-rf-classifier"
)

print(f"Registered model version: {result.version}")

The registered model can be viewed in the MLflow Model Registry.

STEP 9: SELECTION OF BEST MODEL

Based on the comparison table:

- rf-50 gives 0.933 accuracy.
- rf-100 gives 0.967 accuracy.
- rf-150 gives 0.967 accuracy.

The rf-100 model is selected because it provides the same accuracy and F1 score as rf-150 with fewer estimators.

Therefore, rf-100 offers a better balance between performance and efficiency.

STEP 10: BASIC / FREQUENTLY USED MLFLOW COMMANDS

mlflow --help
# Displays MLflow help.

mlflow experiments search
# Lists experiments.

mlflow runs list --experiment-id 0
# Lists runs of an experiment.

mlflow models list
# Lists registered models.

mlflow ui
# Starts the MLflow user interface.

STEP 11: ANALYSIS

1. MLflow successfully tracks machine learning experiments.
2. Parameters and metrics are logged for every training run.
3. Model artifacts are stored for future use.
4. Different model configurations can be compared through the MLflow UI.
5. The best-performing model can be registered for future deployment.

CONCLUSION:

Thus, we have installed and configured MLflow, trained multiple machine learning models, logged their parameters, metrics and artifacts, compared different experiments, registered the best model, and selected the optimal model based on experimental results.

VIVA QUESTIONS AND ANSWERS

1. What is MLflow?
MLflow is an open-source platform used to manage and track machine learning experiments.

2. What is experiment tracking?
Experiment tracking is the process of recording model parameters, metrics and results.

3. What are parameters?
Parameters are values used to configure a machine learning model, such as n_estimators.

4. What are metrics?
Metrics are values used to evaluate model performance, such as accuracy and F1 score.

5. What are artifacts?
Artifacts are files generated during an ML experiment, such as trained models and output files.

6. What is the MLflow UI?
It is a web-based interface used to view and compare experiment runs.

7. What is model registration?
Model registration is the process of storing a trained model in the MLflow Model Registry.

8. What is Random Forest?
Random Forest is an ensemble learning algorithm that combines multiple decision trees to make predictions.

9. What is accuracy?
Accuracy is the ratio of correctly predicted observations to the total observations.

10. Why is rf-100 selected as the best model?
Because it achieves the same accuracy as rf-150 with fewer estimators, reducing computational cost.
