## Installation

1.Create a python 3 environment. All the dependencies of a project should be ported in a Venv
    
    virtualenv -p python3 envname

2.Switch to that environment 
    
    source path-to-env/envname/bin/activate
    
    PS - Install virtualenvwrapper to make the virtual env process easier
    
3.Install requirements from `requirements.txt`. 

Use the requirement files for each environment to install all the requirements in a single step using 

    pip install -r requirements.txt

4.Run flask server

    python run.py

 5.Postman collection is as below

    https://www.getpostman.com/collections/33585c98f09f1b6063df