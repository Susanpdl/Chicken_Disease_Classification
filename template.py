import os  # Importing the os module for interacting with the operating system
from pathlib import Path  # Importing Path from pathlib to handle file paths in a cleaner way
import logging  # Importing logging to display messages while running the script

# Setting up logging configuration to display info messages with timestamps
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Defining the project name, which is used to structure file paths
project_name = "cnnClassifier"

# List of file paths that need to be created
list_of_files = [
    ".github/workflows/.gitkeep",  # A hidden file to keep empty directories in Git
    f"src/{project_name}/__init__.py",  # Init file for the main source directory
    f"src/{project_name}/components/__init__.py",  # Init file for components module
    f"src/{project_name}/utils/__init__.py",  # Init file for utilities module
    f"src/{project_name}/config/__init__.py",  # Init file for config module
    f"src/{project_name}/config/configuration.py",  # Configuration script for the project
    f"src/{project_name}/pipeline/__init__.py",  # Init file for pipeline module
    f"src/{project_name}/entity/__init__.py",  # Init file for entity module
    f"src/{project_name}/constants/__init__.py",  # Init file for constants module
    "config/config.yaml",  # YAML configuration file
    "dvc.yaml",  # DVC (Data Version Control) configuration file
    "params.yaml",  # Parameters file for model training
    "requirements.txt",  # File listing dependencies required for the project
    "setup.py",  # Python setup script for packaging
    "research/trials.ipynb",  # Jupyter Notebook for research and experiments
    "templates/index.html"  # HTML file for the project's frontend (if applicable)
]

# Loop through each file in the list
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert string path to a Path object
    filedir, filename = os.path.split(filepath)  # Separate directory and file name

    # If the directory is not empty, create it if it does not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directories recursively if they don't exist
        logging.info(f"Creating directory; {filedir} for the file: {filename}")  # Log the action

    # If the file does not exist or is empty, create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # Open file in write mode (creates it if it doesn't exist)
            pass  # Do nothing (just create an empty file)
            logging.info(f"Creating empty file: {filepath}")  # Log the action
    else:
        logging.info(f"{filename} already exists")  # Log if the file already exists
