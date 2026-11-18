
EXPERIMENT NO. 10

TITLE: CONTAINERIZATION OF A MACHINE LEARNING APPLICATION USING DOCKER

AIM:
To understand Docker, create a Dockerfile, package a machine learning application, build Docker images, run containers, test containerized applications and document the container deployment process.

DESCRIPTION:
Docker is a containerization platform that packages an application along with its dependencies, libraries and configuration into a single portable image.

It ensures that an ML application runs consistently across different environments such as development, testing and production.

STEP 1: INTRODUCTION TO DOCKER – KEY CONCEPTS

1. Image:
A read-only template containing application code, runtime, libraries and dependencies.

2. Container:
A running instance of an image, isolated from the host system.

3. Dockerfile:
A text file containing instructions to build a Docker image.

4. Docker Hub / Registry:
A repository used for storing and sharing Docker images.

STEP 2: INSTALLATION AND CONFIGURATION

1. Download Docker Desktop from:
https://www.docker.com/products/docker-desktop/

2. Install Docker Desktop on your computer.
3. Start Docker Desktop.
4. Open Command Prompt or VS Code Terminal.
5. Check Docker installation:

docker --version

6. Verify Docker is running:

docker info

STEP 3: CREATE PROJECT STRUCTURE

Create a folder named:

ml-app

Inside it, create the following files:

ml-app/
│
├── app.py
├── model.pkl
├── train_model.py
├── requirements.txt
└── Dockerfile

NOTE:
The manual lists app.py, model.pkl, requirements.txt and Dockerfile. The additional train_model.py file is included to generate model.pkl if you do not already have a trained model.

STEP 4: CREATE REQUIREMENTS.TXT

Add the following libraries:

flask
scikit-learn
numpy

STEP 5: CREATE TRAIN_MODEL.PY

This program trains a simple Iris classification model and saves it as model.pkl.

import pickle

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load Iris dataset
data = load_iris()

X = data.data
y = data.target

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Save trained model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved successfully.")

STEP 6: GENERATE MODEL FILE

Open the terminal inside the ml-app folder.

Execute:

pip install -r requirements.txt

Then execute:

python train_model.py

Expected output:

Model trained and saved successfully.

A file named model.pkl will be created automatically.

STEP 7: CREATE APP.PY

This file loads the trained model and provides a prediction API.

from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Iris class names
class_names = [
    "setosa",
    "versicolor",
    "virginica"
]

@app.route("/")
def home():
    return "ML Application is Running!"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    features = data["features"]

    prediction = model.predict([features])[0]

    probabilities = model.predict_proba([features])[0]

    confidence = float(max(probabilities))

    return jsonify({
        "prediction": class_names[int(prediction)],
        "confidence": round(confidence, 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

STEP 8: TEST APPLICATION LOCALLY

Before creating the Docker image, execute:

python app.py

Open your browser:

http://127.0.0.1:5000

Expected output:

ML Application is Running!

Stop the application using Ctrl + C.

STEP 9: CREATE DOCKERFILE

Create a file named:

Dockerfile

Add the following instructions:

# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose application port
EXPOSE 5000

# Run application
CMD ["python", "app.py"]

STEP 10: BUILD THE DOCKER IMAGE

Open the terminal inside the ml-app folder.

Execute:

docker build -t ml-app:v1 .

Explanation:

docker build - Creates a Docker image.

-t ml-app:v1 - Assigns the image name and version.

. - Uses the current directory as the build context.

Expected output:

[+] Building 8.4s (10/10) FINISHED

[1/5] FROM python:3.10-slim

[2/5] WORKDIR /app

[3/5] COPY requirements.txt .

[4/5] RUN pip install --no-cache-dir -r requirements.txt

[5/5] COPY . .

Exporting to image

Naming to docker.io/library/ml-app:v1

NOTE:
Build time and displayed messages may vary.

STEP 11: RUN THE DOCKER CONTAINER

Execute:

docker run -d -p 5000:5000 --name ml-app-container ml-app:v1

Explanation:

-d = Runs the container in the background.

-p 5000:5000 = Maps host port 5000 to container port 5000.

--name = Assigns a name to the container.

ml-app:v1 = Specifies the Docker image.

STEP 12: VERIFY RUNNING CONTAINER

Execute:

docker ps

Expected example output:

CONTAINER ID   IMAGE       COMMAND          PORTS
7f2a91c4d8b1   ml-app:v1   "python app.py"  0.0.0.0:5000->5000/tcp

NAMES

ml-app-container

STEP 13: TEST THE CONTAINERIZED APPLICATION

Execute the following command in a terminal:

curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"features\": [5.1, 3.5, 1.4, 0.2]}"

Expected output:

{
  "prediction": "setosa",
  "confidence": 1.0
}

NOTE:
The exact confidence value may vary depending on the trained model. The manual shows an example confidence of 0.98.

STEP 14: DOCUMENTATION OF CONTAINER DEPLOYMENT PROCESS

Step 1:
Command: docker build -t ml-app:v1 .
Purpose: Build the image from the Dockerfile.

Step 2:
Command: docker run -d -p 5000:5000 ml-app:v1
Purpose: Start the container in detached mode.

Step 3:
Command: docker ps / docker logs
Purpose: Verify the container is running and debug errors.

Step 4:
Command: curl / Postman request
Purpose: Test the exposed API endpoint.

Step 5:
Command: docker push
Purpose: Publish the image to a registry for deployment.

STEP 15: BASIC / FREQUENTLY USED DOCKER COMMANDS

docker --version
# Check installed Docker version

docker images
# List locally available images

docker ps
# List running containers

docker ps -a
# List all containers, including stopped ones

docker stop ml-app-container
# Stop a running container

docker rm ml-app-container
# Remove a container

docker rmi ml-app:v1
# Remove a Docker image

docker logs ml-app-container
# View container logs

CONCLUSION:

Thus, we have studied Docker fundamentals, created a Dockerfile, packaged a machine learning application into a Docker image, built and ran the image as a container, tested the containerized application and documented the complete container deployment process.

VIVA QUESTIONS AND ANSWERS

1. What is Docker?
Docker is a containerization platform used to package and run applications with their dependencies.

2. What is a Docker image?
A Docker image is a read-only template used to create containers.

3. What is a Docker container?
A container is a running instance of a Docker image.

4. What is a Dockerfile?
A Dockerfile is a text file containing instructions to build a Docker image.

5. What is Docker Hub?
Docker Hub is a cloud-based registry used to store and share Docker images.

6. What is containerization?
Containerization is the process of packaging an application with its dependencies into a container.

7. What is the purpose of the FROM instruction?
FROM specifies the base image used to build a Docker image.

8. What is the purpose of EXPOSE 5000?
It documents the port on which the application listens inside the container.

9. What is the purpose of WORKDIR?
WORKDIR sets the working directory inside the Docker container.

10. What is the difference between an image and a container?
An image is a template, whereas a container is a running instance of that image.

11. What is the purpose of docker build?
It builds a Docker image using instructions from a Dockerfile.

12. What is the purpose of docker run?
It creates and starts a container from a Docker image.

13. What is the purpose of docker ps?
It displays currently running containers.

14. Why is Docker used in MLOps?
Docker ensures consistent execution of ML applications across different environments.
