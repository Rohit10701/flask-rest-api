
Note : The os being used is Arch Linux.
# Getting Started

To test REST Api locally, follow these steps:


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

