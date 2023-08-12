# Project Overview
This project is a collaborative whiteboard.

---
## Setting up the development environment

This project is using poetry as the virtual environment and package management solution.

You can install poetry using pip with the following command:

```pip install poetry```

#### Running the program in Poetry
To enable a shell with this virtual enviroment, run the following command in the directory with the pyproject.toml file ``poetry shell``

Once you are in the shell, you can run any of your project files inside the virtual environment. If you are not in the shell, you can instead run the following command to run something as a one-off: poetry run command

for example, if you want to run main.py: ``poetry run python main.py``

#### Adding dependencies to a Poetry Project

To add a dependency to your project, type the following command into your Poetry Shell. This example will install the requests library. 
``poetry add requests``

This command adds a line to your pyproject.toml file. It adds a line after the [tool.poetry.dependencies] section. For example, the line added for installing requests is: 

requests = "^2.28.1"