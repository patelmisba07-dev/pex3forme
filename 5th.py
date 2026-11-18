
EXPERIMENT NO. 5
TITLE: IMPLEMENTATION OF FEATURE STORE USING FEAST

AIM:
To understand feature stores, create a feature repository,
define and register features, ingest data into the feature
store, retrieve online and offline features, reuse features
for multiple models, and analyse the benefits of feature
stores in MLOps.

--------------------------------------------------
DESCRIPTION:
--------------------------------------------------

A Feature Store is a centralized system for storing, managing
and serving features used in machine learning.

It ensures that the same feature definitions and values are
consistently used during model training (offline/batch) and
real-time inference (online).

Feast (Feature Store) is a popular open-source feature store
used in MLOps pipelines.

--------------------------------------------------
STEP 1: INSTALLATION OF FEAST
--------------------------------------------------

Open VS Code terminal or Command Prompt.

Install Feast:

pip install feast

Check Feast version:

feast --version

--------------------------------------------------
STEP 2: FEATURE REPOSITORY CREATION
--------------------------------------------------

Create a feature repository:

feast init my_feature_repo

Open the repository:

cd my_feature_repo

The repository contains configuration files and a feature
definition file.

Create a folder named data inside the repository.

Project structure:

my_feature_repo/
    |
    |--- feature_store.yaml
    |
    |--- example_repo.py
    |
    |--- customer_features.py
    |
    |--- data/
           |
           |--- customer_stats.parquet

--------------------------------------------------
STEP 3: CREATE SAMPLE FEATURE DATA
--------------------------------------------------

Create a Python file named create_data.py.

Write the following code:

import pandas as pd

data = pd.DataFrame({
    "customer_id": [1001, 1002, 1003],
    "event_timestamp": pd.to_datetime([
        "2026-11-18 08:00:00",
        "2026-11-18 08:00:00",
        "2026-11-18 08:00:00"
    ], utc=True),
    "avg_purchase_amount": [452.75, 320.50, 600.00],
    "total_orders": [18, 12, 25]
})

data.to_parquet("data/customer_stats.parquet", index=False)

print("Feature data created successfully.")

Execute:

python create_data.py

NOTE:
The sample data file must be created before registering
and materializing the features.

--------------------------------------------------
STEP 4: FEATURE DEFINITION AND REGISTRATION
--------------------------------------------------

Create a Python file named customer_features.py.

Write the following code:

from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, Int64
from datetime import timedelta

# Define customer entity
customer = Entity(
    name="customer_id",
    join_keys=["customer_id"]
)

# Define data source
customer_stats_source = FileSource(
    path="data/customer_stats.parquet",
    timestamp_field="event_timestamp",
)

# Define feature view
customer_stats_fv = FeatureView(
    name="customer_stats",
    entities=[customer],
    ttl=timedelta(days=30),
    schema=[
        Field(name="avg_purchase_amount", dtype=Float32),
        Field(name="total_orders", dtype=Int64),
    ],
    source=customer_stats_source,
)

Register the entities and feature views:

feast apply

Expected output:

Created entity customer_id
Created feature view customer_stats
Deploying infrastructure for customer_stats

--------------------------------------------------
STEP 5: DATA INGESTION INTO THE FEATURE STORE
--------------------------------------------------

Execute the following command using Linux or Git Bash:

feast materialize-incremental $(date -u +"%Y-%m-%dT%H:%M:%S")

Purpose:

This command ingests the latest feature values into the
online feature store.

--------------------------------------------------
STEP 6: RETRIEVAL OF OFFLINE FEATURES (FOR TRAINING)
--------------------------------------------------

Create a Python file named offline_features.py.

Write the following code:

from feast import FeatureStore
import pandas as pd

# Connect to feature store
store = FeatureStore(repo_path=".")

# Create entity dataframe
entity_df = pd.DataFrame({
    "customer_id": [1001, 1002, 1003],
    "event_timestamp": pd.Timestamp.now(tz="UTC"),
})

# Retrieve historical features
training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "customer_stats:avg_purchase_amount",
        "customer_stats:total_orders"
    ],
).to_df()

print(training_df)

Execute:

python offline_features.py

Purpose:

Offline features are used during model training and
historical analysis.

--------------------------------------------------
STEP 7: RETRIEVAL OF ONLINE FEATURES
(FOR REAL-TIME INFERENCE)
--------------------------------------------------

Create a Python file named online_features.py.

Write the following code:

from feast import FeatureStore

# Connect to feature store
store = FeatureStore(repo_path=".")

# Retrieve online features
online_features = store.get_online_features(
    features=[
        "customer_stats:avg_purchase_amount",
        "customer_stats:total_orders"
    ],
    entity_rows=[
        {"customer_id": 1001}
    ],
).to_dict()

print(online_features)

Execute:

python online_features.py

Expected example output:

{
    'customer_id': [1001],
    'avg_purchase_amount': [452.75],
    'total_orders': [18]
}

Purpose:

Online features are used for real-time model predictions.

--------------------------------------------------
STEP 8: FEATURE REUSABILITY FOR MULTIPLE MODELS
--------------------------------------------------

Once registered, the customer_stats feature view can be
referenced by multiple model training scripts and serving
applications without redefining the feature logic.

Benefits:

1. Features can be reused by multiple models.
2. Reduces duplicate work.
3. Maintains consistency across teams.
4. Saves development time.

--------------------------------------------------
STEP 9: BENEFITS OF FEATURE STORES IN MLOPS
--------------------------------------------------

1. Eliminates training-serving skew by using the same
   feature definitions for training and inference.

2. Promotes feature reuse across multiple models and teams.

3. Provides point-in-time correctness for historical
   feature retrieval, helping avoid data leakage.

4. Speeds up experimentation because engineers can
   browse and reuse existing features.

5. Centralizes governance and monitoring of feature quality.

--------------------------------------------------
STEP 10: BASIC AND FREQUENTLY USED FEAST COMMANDS
--------------------------------------------------

Display Feast help:

feast --help

Check Feast version:

feast --version

List registered entities:

feast entities list

List registered feature views:

feast feature-views list

Remove deployed feature store infrastructure:

feast teardown

--------------------------------------------------
STEP 11: ANALYSIS OF RESULTS
--------------------------------------------------

1. Feast was installed successfully.
2. A feature repository was created.
3. Customer entity and feature view were defined.
4. Features were registered using feast apply.
5. Feature values were ingested into the online store.
6. Historical features were retrieved for training.
7. Online features were retrieved for real-time inference.
8. Feature reusability and benefits were studied.

--------------------------------------------------
STEP 12: CONCLUSION
--------------------------------------------------

Thus, we have studied the concept of feature stores,
created a feature repository, defined and registered
features, ingested data into the store, retrieved both
offline and online features, and analysed the benefits
of feature stores in an MLOps workflow.

--------------------------------------------------
IMPORTANT VIVA QUESTIONS AND ANSWERS
--------------------------------------------------

1. What is a Feature Store?
   A centralized system for storing, managing and serving
   machine learning features.

2. Which Feature Store tool is used in this experiment?
   Feast.

3. What is Feast?
   Feast is an open-source feature store used in MLOps.

4. What is a feature?
   A feature is an input variable used by a machine
   learning model.

5. What is a feature repository?
   It is a project directory containing feature definitions
   and configuration files.

6. What is an Entity in Feast?
   An entity represents an object, such as a customer,
   associated with features.

7. What is a Feature View?
   It defines a group of related features and their source.

8. What is FileSource?
   It specifies a file-based data source for features.

9. What does feast apply do?
   It registers entities and feature views.

10. What is data ingestion?
    It is the process of loading feature data into a
    feature store.

11. What is an offline feature store?
    It stores historical features mainly used for model
    training and analysis.

12. What is an online feature store?
    It serves feature values for real-time inference.

13. What is training-serving skew?
    It is the difference between feature processing during
    training and during real-time inference.

14. What does get_historical_features() do?
    It retrieves historical features for model training.

15. What does get_online_features() do?
    It retrieves online features for real-time inference.

16. What is feature reusability?
    It means using the same registered features across
    multiple machine learning models.

17. What is point-in-time correctness?
    It ensures that historical training data uses only
    feature values available at the relevant time.

18. What is TTL?
    TTL stands for Time To Live. It defines how long
    feature data remains valid for retrieval.

19. Why are Feature Stores important in MLOps?
    They maintain feature consistency, support reuse and
    simplify feature management.

20. What does feast teardown do?
    It removes deployed feature store infrastructure.
