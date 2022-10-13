# when trying to install with pip but getting SSL errors: 
# pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <package_name>


# using virtual environments with github https://www.youtube.com/watch?v=6W6iY7uUu34 
# After completing work in a venv and ready to upload to VCS
# pip freeze > requirements.txt will create a requirements.txt file with your currently installed packages into the dir
# add the requirements.txt along with 
# to install these packages in a cloned venv, run: install -r requirements.txt
# after a venv has been created (ideally in the github repo) clone repo then activate env with ~PATHTOVENV/VENVNAME/Script/activate.bat
# the name of the venv should show in command prompt at the beginning of the cmd line

# $ git clone <Project A>  # Cloning project repository
# $ cd <Project A> # Enter to project directory
# $ python -m venv my_venv # If not created, creating virtualenv
# $ source ./my_venv/bin/activate # Activating virtualenv
# (my_venv)$ pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt # Installing dependencies from requirements.txt
# (my_venv)$ deactivate # When you want to leave virtual environment