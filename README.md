
<<<<<<< HEAD
# Check Data App

The **Check Data App** is a web application built with Dash that allows users to upload and interactively explore data files (CSV or Excel). Users can view various details about the uploaded data, such as the first few rows, data types, missing values, and descriptive statistics. The app is built with Dash and Pandas and is Docker-ready for easy deployment.

## Features

- **File Upload**: Allows users to upload CSV or Excel files.
- **Data Analysis Options**:
  - **Head**: Displays the first few rows of data.
  - **Info**: Shows column data types and memory usage.
  - **Tail**: Displays the last few rows of data.
  - **Shape**: Provides the dataset dimensions (rows and columns).
  - **Describe**: Offers summary statistics for numerical columns.
  - **Dtypes**: Lists the data types for each column.
  - **Show Data**: Displays the entire dataset.
  - **Check Missing Values**: Shows the count of missing values per column.
  - **Close Tab**: Clears the current display.

[Include some screenshots of your app's UI and functionality]
<h3>Application Screenshots</h3>
<p align="center">
  <img src="assets\mainScreen.jpg" width="300" />
  <img src="assets\Head.jpg" width="300" />
  <img src="assets\tail.jpg" width="300" />
</p>


## Project Structure

```
.
├── app.py                 # Main application code
├── Dockerfile             # Docker configuration for containerized deployment
├── docker-compose.yml     # Docker Compose configuration for multi-container setups
└── README.md              # Project documentation
```

## Setup and Installation

### Prerequisites

- **Python 3.9+**
- **Docker** (optional, for containerized deployment)

### Local Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   ```bash
   pip install dash dash-bootstrap-components pandas
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

### Docker Installation

#### Dockerfile

The `Dockerfile` is configured to build an environment for running the app in a Docker container:

```Dockerfile
# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8050

# Run the application
CMD ["python", "app.py"]
```

#### Docker Compose

The `docker-compose.yml` file simplifies Docker configuration for running the app:

```yaml
version: '3'

services:
  check_data_app:
    build: .
    ports:
      - "8050:8050"
    volumes:
      - .:/app
```

To run the app with Docker Compose:
```bash
docker-compose up
```

## Usage

### 1. Upload a File
Click on the "Upload" button to upload a CSV or Excel file. After uploading, the file name will be displayed in the file details section.

### 2. Explore Data
Use the available buttons to view specific aspects of your data:
- **Head**: Shows the top rows of the dataset.
- **Info**: Displays data types and memory usage for each column.
- **Tail**: Shows the bottom rows of the dataset.
- **Shape**: Provides the number of rows and columns in the dataset.
- **Describe**: Displays summary statistics for numerical columns.
- **Dtypes**: Lists the data types of each column.
- **Show Data**: Displays the full dataset in a table.
- **Check Missing Values**: Lists missing value counts for each column.
- **Close Tab**: Clears the output display.

## Code Explanation

### File Upload and Storage

The `dcc.Upload` component allows users to upload files. Uploaded files are stored in JSON format, making them accessible across the app.

```python
@app.callback(
    [Output('stored-data', 'data'), Output('file-details', 'children')],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename')]
)
def upload_funct(contents, filename):
    # Processes the file and stores the data in JSON format
```

### Data Display

Each button triggers a callback to display the requested data or summary in the `output-container`.

```python
@app.callback(
    Output('output-container', 'children'),
    [Input('btn-head', 'n_clicks'), Input('btn-info', 'n_clicks'), ...],
    [State('stored-data', 'data')]
)
def display_operation(...):
    # Displays head, tail, info, or other data summaries based on button clicks
```

## Troubleshooting

- Ensure Docker is running if deploying via Docker.
- If any component fails to load, check the console for errors regarding missing files or unsupported formats.

## Technologies Used

- **Dash**: A Python framework for building interactive web applications.
- **Pandas**: A data manipulation and analysis library.
- **Bootstrap**: Used for styling via Dash Bootstrap Components.

---

This README provides a clear overview of the Check Data App’s functionality, setup instructions, and code structure for easy usage and deployment.
=======
>>>>>>> 762ab65b4e0dc48ec37a74b484f6a2cd994dc7ab
