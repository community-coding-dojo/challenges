# Virtual Environment

Virtual environments are a nice way of encapsulating project dependencies without cluttering your system installation
of python. Recommended whenever you need to install extra python packages.

## Setup Instructions

## Linux

1. Make sure, the package python-virtualenv is installed. E.g. on Ubuntu: `sudo apt install python-virtualenv`
2. Create a new venv in the directory ./venv with the following command:

    ```sh
    virtualenv -p python3 ./venv
    ```
3. Activate the virtual environment (Required whenever you want to work on your project):

    ```sh
    source ./venv/bin/activate
    ```
   
## Windows

1. Create a new venv in the directory .\venv with the following command:

    ```sh
    python3 -m venv ./venv
    ```
3. Activate the virtual environment (Required whenever you want to work on your project):

    ```sh
    venv\Scripts\activate.bat
    ```
