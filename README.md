# Dockerless CI/CD Project

## Project Overview

This project demonstrates a Docker-free Continuous Integration and Continuous Delivery (CI/CD) workflow using Python, Jenkins, GitHub, and SonarQube.

The pipeline is designed to retrieve application code from GitHub, run automated tests, and analyze code quality using SonarQube.

## Objectives

- Build a Python web application.
- Run automated unit tests.
- Store source code in Git and GitHub.
- Automate build and test steps using Jenkins.
- Analyze source code quality using SonarQube.
- Practice CI/CD concepts without Docker.

## Technology Stack

- **Programming Language:** Python
- **Version Control:** Git and GitHub
- **CI/CD:** Jenkins
- **Code Quality:** SonarQube
- **Operating System:** Ubuntu on AWS EC2 and Windows for local development

## Project Structure

```text
Dockerless-CI-CD-Project/
├── app.py
├── test_app.py
├── sonar-project.properties
├── Jenkinsfile
├── requirements.txt
└── README.md
```

## Application Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Returns the application status and welcome message |
| `/health` | Returns the application health status |

The application runs locally on `http://127.0.0.1:8000` during development.

## Run the Application

```bash
python app.py
```

## Run Automated Tests

```bash
python -m unittest -v test_app.py
```

## CI/CD Workflow

1. Developer pushes code to GitHub.
2. Jenkins checks out the repository.
3. Automated tests run.
4. SonarQube analyzes source code quality.
5. Jenkins reports the pipeline result.

## Deployment Architecture

- **Development:** Windows and VS Code
- **Source Control:** GitHub
- **CI/CD Server:** Jenkins on AWS EC2
- **Code Analysis:** SonarQube on AWS EC2
- **Containerization:** Not required

## Learning Outcomes

This project provides hands-on practice with Git workflows, Python testing, Jenkins pipelines, SonarQube integration, and AWS-based DevOps tooling.

## Author

Mohan Kumar Reddy

**Note:** This project is a learning implementation. Pipeline automation and SonarQube analysis will be verified as the remaining stages are configured.