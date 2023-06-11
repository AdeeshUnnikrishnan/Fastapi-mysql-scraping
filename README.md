# Fastapi-mysql-scraping
This application demonstrates the integration of FastAPI, MySQL, web scraping, and Docker. It allows you to perform web scraping operations and store the scraped data in a MySQL database. The application is containerized using Docker for easy deployment and scalability.

# Description
The application is built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.9. It utilizes the SQLAlchemy library for interacting with the MySQL database. The web scraping functionality is implemented using Selenium and requests libraries.

Endpoints
This application provides the following endpoints:

# Create User: /create-user

  * Description: Creates a new user in the system.
  * Method: POST
# Get User: /get-user/{user_id}

  * Description: Retrieves user information by user ID.
  * Method: GET
# Delete User: /delete-user/{user_id}

  * Description: Deletes a user by user ID.
  * Method: DELETE
# Update User: /update-user/{user_id}

  * Description: Updates user information by user ID.
  * Method: PUT
# Scraping: /scraping

  * Description: Performs web scraping operation.
  * Method: POST

# Docker and MySQL Workbench/Server Installation
  To run this application using Docker and MySQL Workbench/Server, follow these instructions:

   * Install Docker: Visit the official Docker website (https://www.docker.com/) and follow the installation instructions for your operating system.

   *  Install MySQL Workbench/Server: Visit the official MySQL website (https://www.mysql.com/) and download the appropriate version of MySQL Workbench and MySQL Server for your operating system. Follow the installation instructions provided.
 
# Docker Deployment
   * To deploy the FastAPI MySQL Web Scraping application using Docker, follow the steps below:

      * Install Docker: Visit the official Docker website (https://www.docker.com/) and follow the installation instructions for your operating system.

      * Clone the application repository: Clone the repository containing the FastAPI MySQL Web Scraping application code to your local machine.

      *  Navigate to the project directory: Open a terminal or command prompt and navigate to the directory where the project files are located.

      * Build and run the Docker containers: Execute the following command to build and run the Docker containers:
                                        docker-compose up --build
      * This command will build the Docker images for the application and its dependencies, create and start the containers.

      * Access the application: Once the Docker containers are running, you can access the FastAPI endpoints by opening a web browser and navigating to                   http://localhost:8000.

      # Note: Depending on your Docker configuration, you may need to adjust the port number if you have made changes to the Docker Compose file.

      * You can now make requests to the FastAPI endpoints and interact with the application.

      * Additionally, the MySQL server is accessible at localhost:3307 (or the specified port) if you need to connect to it using MySQL Workbench or any other             MySQL client.

# Running the Application
    To run the application, follow these steps:

    Ensure that the required packages are installed as mentioned in the "Package Details and Installation Instructions" section.

    Optionally, you can run the main.py (to run without docker) file located in the parent directory using the following command:
    * create a venv to activate virtual environment, python -m venv venv
    * python main.py

## Package Details and Installation Instructions

This application requires the following packages:

- selenium
- requests
- sqlalchemy
- mysql.connector
- pydantic
- pymysql
- uvicorn
- webdriver_manager
- pandas
- fastapi

To install the packages, run the following command:

```bash
pip install selenium requests sqlalchemy mysql-connector-python pydantic pymysql uvicorn webdriver_manager pandas fastapi 

