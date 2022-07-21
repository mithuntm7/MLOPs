MLOPs Pipeline
==============================

CI Steps for ML

Project Organization
------------
    ├── Makefile           <- Makefile for installation of all the dependencies using `make install` 
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               <- tracked using dvc, only .dvc available on github, actual data linked with google drive using dvc
    ├── models             <- Trained and pickled models
    ├── reports            <- Generated train and test metrics and tracked using dvc
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment
    ├── src                <- Source code for use in this project.
    │   ├── train.py       <- for training the model and storing the model file, logging the training metrics
    │   └── test.py        <- for testing the model and tracking the model metrics using dvc
    ├── .github/workflows  <- train.yaml file for triggering installations, model error calculations and logging using dvc
    ├── .dvc               <- contains dvc remote storage configuration (google drive)
    ├── dvc.yaml           <- dvc repro stages - model training, model testing, metrics loggging 
    └── dvc.lock           <- dvc repro stages meta data info

--------

Random Forest classifier is trained for predicting the labels of Iris DataSet

GitHub Repository : https://github.com/mithun-tm/MLOPs

Features
1. Github integration of all the development files : Continuous Integration
2. CookieCutter format for organizing the repository
3. Github workflows for triggering commands on every push
4. DVC integration
5. Tracking of train.csv and test.csv using DVC, added google drive as remote storage
6. Stages are defined with train, test and metrics. Metrics tracked by DVC
7. DVC repro in GitHub workflow for tracking metrics from different ML experiments facilitating continuous machine learning
8. AWS Cloud9 for using a cloud server which would help in migrating the workflow to the cloud, deployment on cloud

Changes in the model param from an experiment branch would result in a comparison of the experiment model's metrics with the production model's metrics.

<img width="942" alt="image" src="https://user-images.githubusercontent.com/108567882/177427539-efb0eb96-3940-4170-8bfa-802cf6be98b7.png">


Cloned the GitHub repo to the server on cloud9

<img width="1505" alt="image" src="https://user-images.githubusercontent.com/108567882/177424795-e1e29288-5695-4696-9339-b1dad57bda38.png">

