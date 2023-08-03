
Note : The os being used is Arch Linux.

# Installing Dependencies
  ```bash
    pip install -r requirements.txt
  ```
  
# Procedure
Step-1: Creating virtual enviroment
  ```bash
    python -m venv myenv
    source source myenv/bin/activate
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

