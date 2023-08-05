
Note : The os being used is Arch Linux.
# Getting Started
This project is a Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API. The application provides HTTP endpoints to interact with the User resource, allowing users to manage user data efficiently.

To test REST Api locally, follow these steps:

## Requirements :
1. You should have pyhton 3.10 or above
2. you should have docker installed

To install it [Arch linux]:
```bash
  sudo pacman -Syu
```
```bash
  sudo pacman -S python
  sudo pacman -S python-pip
```
```bash
  sudo pacman -S docker
```




# Clone the repository:
```bash
git clone https://github.com/Rohit10701/Assignment.git
```
# Navigate to the project directory:
```bash
cd <repository>
```

# Installing Dependencies
  ```bash
    pip install -r requirements.txt
  ```
  
# Procedure
Step-1: Creating virtual enviroment
  ```bash
    python -m venv myenv
    source myenv/bin/activate
  ```

Step-2: Installing libraries
  ```bash
    pip install -r requirements.txt
  ```

Step-3: Run
```bash
  > export PYTHONDONTWRITEBYTECODE=1 FLASK_APP="app" FLASK_ENV="development"
  > flask run
```

# Dockerize 
Step-1: Build Docker image
```bash
  sudo docker build -t corider-restapi-rohit .
```

Step-2: Run docker
```bash
  sudo docker run -d -p 5000:5000 corider-restapi-rohit flask run --host=0.0.0.0
```
To check the status :
```bash
  sudo docker ps
```

To close the docker image:
```bash
  sudo docker stop <container_id>
```

# Reference for flask-restful
1. https://flask-restful.readthedocs.io/en/latest/quickstart.html
2. https://marshmallow.readthedocs.io/en/stable/quickstart.html
3. https://realpython.com/flask-blueprint/#what-a-flask-application-looks-like