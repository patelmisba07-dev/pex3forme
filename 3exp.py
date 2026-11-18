
EXPERIMENT NO. 3
TITLE: INSTALLATION AND CONFIGURATION OF DVC FOR DATASET VERSIONING

AIM:
To perform installation and configuration of DVC, dataset tracking,
dataset version management, storage of data artifacts, comparison
of dataset versions, integration of DVC with Git, and reproducibility
of machine learning experiments.

--------------------------------------------------
DESCRIPTION:
--------------------------------------------------

DVC (Data Version Control) is an open-source tool that extends Git
to handle large datasets, ML models and pipelines.

Git tracks code and small DVC metadata files, while DVC tracks
large data files and stores them in separate storage.

This helps in managing dataset versions and reproducing ML
experiments.

--------------------------------------------------
STEP 1: INSTALLATION AND CONFIGURATION OF DVC
--------------------------------------------------

Open VS Code terminal or Command Prompt.

Install DVC:

pip install dvc

Check DVC version:

dvc --version

Create a project folder:

mkdir ml-project

Open the folder:

cd ml-project

Initialize Git repository:

git init

Configure Git username and email:

git config --global user.name "YourName"

git config --global user.email "you@example.com"

Initialize DVC:

dvc init

Add DVC configuration files to Git:

git add .dvc .dvcignore .gitignore

Commit the changes:

git commit -m "Initialize DVC"

--------------------------------------------------
STEP 2: DATASET TRACKING
--------------------------------------------------

Create a folder named data.

Inside the data folder, create a file named train.csv.

Example train.csv content:

name,age,income
A,20,20000
B,25,30000
C,30,40000

Track the dataset using DVC:

dvc add data/train.csv

This creates:

data/train.csv.dvc

It also adds data/train.csv to .gitignore.

Add the DVC metadata and Git ignore file:

git add data/train.csv.dvc data/.gitignore

Commit the changes:

git commit -m "Track train.csv with DVC"

--------------------------------------------------
STEP 3: STORAGE OF DATA ARTIFACTS (REMOTE STORAGE)
--------------------------------------------------

Configure a local remote storage:

dvc remote add -d myremote /mnt/dvc-storage

The remote storage can also be configured using an S3
or Google Drive URL.

Upload dataset to remote storage:

dvc push

Download dataset from remote storage:

dvc pull

NOTE:
The remote storage folder must be accessible. On Windows,
use a valid local folder path if /mnt/dvc-storage is unavailable.

--------------------------------------------------
STEP 4: DATASET VERSION MANAGEMENT
--------------------------------------------------

After modifying or updating the dataset, execute:

dvc add data/train.csv

Add the updated DVC metadata:

git add data/train.csv.dvc

Commit the updated dataset version:

git commit -m "Update dataset to version 2"

Create a Git tag for version 2:

git tag -a v2-dataset -m "Dataset version 2"

For comparison with version 1, create its tag when committing
the original dataset version:

git tag -a v1-dataset -m "Dataset version 1"

--------------------------------------------------
STEP 5: COMPARISON OF DATASET VERSIONS
--------------------------------------------------

View dataset history:

git log data/train.csv.dvc

Restore the DVC metadata of version 1:

git checkout v1-dataset -- data/train.csv.dvc

Restore the corresponding dataset:

dvc checkout

Compare two dataset versions:

dvc diff v1-dataset v2-dataset

Expected result:

Modified:
data/train.csv

Path          Size          Hash
data/train.csv  Changed      Different hash

--------------------------------------------------
STEP 6: INTEGRATION OF DVC WITH GIT
--------------------------------------------------

DVC and Git work together.

Git tracks:
1. Source code.
2. Small .dvc metadata files.
3. Configuration and version history.

DVC tracks:
1. Large datasets.
2. ML model files.
3. Data artifacts stored in remote storage.

Operations:

1. Track the dataset using dvc add.
2. Add the generated .dvc file to Git.
3. Commit changes using git commit.
4. Upload data using dvc push.
5. Restore a Git version using git checkout.
6. Restore its corresponding dataset using dvc checkout.

--------------------------------------------------
STEP 7: REPRODUCIBILITY OF ML EXPERIMENTS
--------------------------------------------------

Re-run the DVC pipeline if dependencies change:

dvc repro

Display the pipeline dependency graph:

dvc dag

By combining a specific Git commit (code) with a specific
DVC-tracked data version, past experiments can be reproduced.

--------------------------------------------------
STEP 8: BASIC AND FREQUENTLY USED DVC COMMANDS
--------------------------------------------------

Display DVC help:

dvc --help

Check the status of tracked data:

dvc status

List files tracked in a DVC repository:

dvc list <repo>

Download a file without tracking it:

dvc get <repo> <path>

Display tracked metrics:

dvc metrics show

List configured remote storage:

dvc remote list

Check DVC version:

dvc --version

Upload data:

dvc push

Download data:

dvc pull

--------------------------------------------------
STEP 9: ANALYSIS OF RESULTS
--------------------------------------------------

1. DVC was successfully installed and configured.
2. A dataset was tracked using DVC.
3. Dataset metadata was stored in Git.
4. Data artifacts were stored in remote storage.
5. Dataset versions were managed using Git and DVC.
6. Different dataset versions were compared.
7. DVC and Git integration helped maintain reproducibility.

--------------------------------------------------
STEP 10: CONCLUSION
--------------------------------------------------

Thus, we successfully installed and configured DVC, tracked
and versioned a dataset, stored data artifacts in remote
storage, compared different dataset versions, integrated
DVC with Git, and understood how this combination enables
reproducibility of machine learning experiments.

--------------------------------------------------
IMPORTANT VIVA QUESTIONS AND ANSWERS
--------------------------------------------------

1. What is DVC?
   DVC stands for Data Version Control. It is used to track
   and manage large datasets and ML models.

2. Why is DVC used in MLOps?
   It helps manage dataset versions and reproduce ML experiments.

3. What is Git?
   Git is a version control system used to track source code changes.

4. What is the difference between Git and DVC?
   Git tracks source code and metadata, whereas DVC tracks
   large datasets and ML artifacts.

5. What is dataset versioning?
   It is the process of maintaining different versions of
   a dataset.

6. What does dvc init do?
   It initializes DVC in a Git repository.

7. What does dvc add do?
   It starts tracking a dataset using DVC.

8. What is a .dvc file?
   It is a metadata file containing information about a
   DVC-tracked data file.

9. What does dvc push do?
   It uploads tracked data to remote storage.

10. What does dvc pull do?
    It downloads tracked data from remote storage.

11. What is remote storage?
    It is a separate storage location used to store large
    datasets and artifacts.

12. What does dvc checkout do?
    It restores the data corresponding to the checked-out
    DVC metadata.

13. What does dvc diff do?
    It compares different versions of datasets.

14. What does dvc repro do?
    It reruns the DVC pipeline when dependencies change.

15. What does dvc dag do?
    It displays the pipeline dependency graph.

16. What is reproducibility?
    It means obtaining consistent experiment results using
    the same code and dataset versions.

17. Why does DVC work with Git?
    Git manages code and metadata, while DVC manages large
    data files.

18. What is a Git tag?
    A Git tag identifies a specific point or version in
    the repository history.

19. What is dvc status?
    It checks whether tracked data has changed.

20. Name some remote storage options supported by DVC.
    Local storage, Amazon S3 and Google Drive.
