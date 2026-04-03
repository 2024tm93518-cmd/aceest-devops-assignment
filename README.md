# ACEest Fitness DevOps Assignment

## Project Overview

This project demonstrates a DevOps pipeline for a Flask-based fitness management API.

The application allows basic operations such as:

- Viewing gym members
- Adding new members
- Health check endpoint

The project implements modern DevOps practices including version control, automated testing, containerization, and CI/CD pipelines.

---

## Technologies Used

- Flask
- Pytest
- Docker
- GitHub Actions
- Jenkins

---

## Local Setup

Clone the repository

git clone https://github.com/username/aceest-devops-assignment.git

Install dependencies

pip install -r requirements.txt

Run the application

python app.py

Open browser:

http://localhost:5000

---

## Running Tests

Run the following command:

pytest

---

## Docker Container

Build Docker image

docker build -t aceest-fitness .

Run container

docker run -p 5000:5000 aceest-fitness

---

## CI/CD Pipeline

GitHub Actions automatically runs when code is pushed.

Pipeline stages include:

1. Checkout repository
2. Install dependencies
3. Run automated tests
4. Build Docker image

---

## Jenkins Integration

Jenkins is used as a build server to pull the repository and execute:

- dependency installation
- unit testing
- Docker build

This ensures code integrity before deployment.