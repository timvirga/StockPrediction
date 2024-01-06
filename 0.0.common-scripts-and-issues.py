# when trying to install with pip but getting SSL errors: 
# pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <package_name>


# using virtual environments with github https://www.youtube.com/watch?v=6W6iY7uUu34 

# After completing work in a venv and ready to upload to VCS
# pip freeze > requirements.txt will create a requirements.txt file with your currently installed packages into the dir
# add the requirements.txt along with 
# to install these packages in a cloned venv, run: install -r requirements.txt
# after a venv has been created (ideally in the github repo) clone repo then activate env with ~PATHTOVENV/VENVNAME/Script/activate.bat
# the name of the venv should show in command prompt at the beginning of the cmd line


## Create and clone project repository from github
# add readme and python .gitignore template
# Open git bash terminal (through vscode or wherever) and $ git clone <Project A>  

## create a virtual environment ##

# $ cd <Project A> # Enter to project directory
# open anaconda cmd prompt and create a venv in the working dir with: python -m venv venvname ## or create from python installed on os using below line
#### $ python -m venv my_venv # If not created, creating virtualenv ####
# cd to $ ./my_venv/Scripts/ #
# Activate virtualenv with activate.bat
# cd .. back to working dir
# upgrade pip in new environment (this command on windows) python -m pip install --upgrade pip
# (my_venv)$ pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt # Installing dependencies from requirements.txt
# (my_venv)$ deactivate # When you want to leave virtual environment