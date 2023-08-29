# djangosub

Welcome to the My Django Application documentation. 

This tutorial will show you how to create and operate the application using Docker, running the command and a virtual environment (venv).

## 1. Clone My Repository

Use The Following: git clone https://github.com/cas17/djangosub.git

## 2.Create You virtual enviroment

This is fow Windows(Please Use The Relevant Format According To The Operating System On Your PC):
python3 -m venv venv
venv\Scripts\activate

## 3.Install Required Dependancies

pip install -r requirements.txt

## 4.Running With Docker

### 1. Clone Repository

git clone https://github.com/cas17/djangosub.git

### 2. Build Docker-Image:

docker build -t djangosubby-app .

### 3. Running the Docker:

docker run -p 8000:8000 djangosubby-app

### 4. Stopping Docker:

This is dependant on your system. You can try:

docker ps



# I Hope This Assists You! Happy Coding!

