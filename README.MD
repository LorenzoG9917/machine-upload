# MachineUpload
![UploadMachine](/images/logo.PNG)
## Description
This project is designed to upload information from a [Cloud SQL](http://cloud.google.com/sql) instance (using **MySQL**) to [BigQuery](https://cloud.google.com/bigquery).

## Objective
The main objective of this project is to create a user-friendly program that allows users to interactively connect to their Cloud SQL database, view all the available tables, and upload data from those tables to BigQuery.

## Requirements
- Google Cloud Platform account to use Cloud SQL and BigQuery
- Python installed on your local machine
- Text editor (e.g., Visual Studio Code, Sublime Text) 

## Getting started
- Create a new folder for the project and set up a virtual environment:
```shell
mkdir upload_project
cd upload_project
python -m venv env
```
- Activate the virtual environment (for Windows):
```shell
env/Scripts/activate
```
- Install the required libraries from the requirements.txt file:
```shell
pip install -r requirements.txt
```
- Run the application
```shell
python main.py
```

The application will prompt the user to provide the correct information to establish a connection to the database, including the database user, password, host (IP Address), and name of the database.

## Support
For any support or questions, please contact us at: lguerrerogomez30@gmail.com
## Author
This project was developed by Lorenzo Guerrero.
[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/lorenzoguerrero17/)
&nbsp;
