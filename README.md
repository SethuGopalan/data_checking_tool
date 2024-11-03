Check Data App
The Check Data App is a Dash-based web application that allows users to upload and explore data files (CSV or Excel) interactively.
Users can view different details of the uploaded data, such as the first few rows, data types, missing values, and descriptive statistics.
This app is built using Dash and Pandas and can be deployed using Docker.

Features
  File Upload: Upload CSV or Excel files.
  Data Analysis Options:
  Head: Displays the first few rows of data.
  Info: Shows column data types and memory usage.
  Tail: Displays the last few rows of data.
  Shape: Shows the dataset dimensions.
  Describe: Provides summary statistics.
  Dtypes: Lists data types for each column.
  Show Data: Displays the entire dataset.
  Check Missing Values: Displays missing value counts.
  Close Tab: Clears the current display.
  
Project Structure


├── app.py                 # Main application code
├── Dockerfile             # Docker configuration for the app
├── docker-compose.yml     # Docker Compose configuration
└── README.md              # Project documentation

Setup and Installation

Prerequisites

Python 3.9+
Docker (for containerized deployment)

Local Installation
Clone the Repository:

git clone <repository-url>
cd <repository-directory>

Install Dependencies:

pip install dash dash-bootstrap-components pandas

Run the Application:

python app.py

Docker Installation

Dockerfile

The Dockerfile builds an environment to run the app in a Docker container:

Dockerfile
Copy code
# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port
EXPOSE 8050

# Run the application
CMD ["python", "app.py"]

Docker Compose

The docker-compose.yml file simplifies Docker configuration:

yaml
Copy code
version: '3'

services:
  check_data_app:
    build: .
    ports:
      - "8050:8050"
    volumes:
      - .:/app
To run the app with Docker Compose:
docker-compose up

Usage
1. Upload a File
Drag and drop or select a CSV/Excel file using the "Upload" button. Successful uploads show the filename in the file details section.

3. Explore Data
   
Use the buttons to view specific aspects of your data:
Head: Shows the top rows of the data.
Info: Lists data types and memory information.
Tail: Shows the bottom rows of the data.
Shape: Provides the row and column count.
Describe: Gives summary statistics for numerical data.
Dtypes: Lists each column’s data type.
Show Data: Displays the entire dataset.
Check Missing Values: Counts any missing values per column.
Close Tab: Clears the output section.

Example Code Explanation

File Upload and Storage
The dcc.Upload component allows users to upload files. The contents are stored in JSON format for use across the app.


@app.callback(
    [Output('stored-data', 'data'), Output('file-details', 'children')],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename')]
)
def upload_funct(contents, filename):
    # Processes the file and stores the data in JSON format
Data Display
Each button click triggers a callback to display the requested data summary:


@app.callback(
    Output('output-container', 'children'),
    [Input('btn-head', 'n_clicks'), Input('btn-info', 'n_clicks'), ...],
    [State('stored-data', 'data')]
)
def display_operation(...):
    # Displays head, tail, or info based on the button clicked
Troubleshooting
Ensure Docker is running if deploying via Docker.
Check console logs for any errors related to missing files or incorrect formats.
Technologies Used
Dash: Web framework for building data applications in Python.
Pandas: Data manipulation and analysis.
Bootstrap: UI styling via Dash Bootstrap Components.
