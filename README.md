
# Paragraph API Setup Guide

## Prerequisites
Before you begin, ensure you have the following installed on your system:
- Docker
- Git

## Step 1: Clone the Repository
1. Open your terminal (Command Prompt, PowerShell, or Terminal).
2. Clone the repository using Git:

    
  Command:  git clone https://github.com/vaidehibhonge11/Codemonk_Backend_Assignment
    

3. Navigate into the cloned repository directory:

    
  Command: cd Codemonk_Backend_Assignment
    

## Step 2: Build and Start Docker Containers
1. In the terminal, navigate into the cloned repository directory (if not already there):

    
  Command: cd Codemonk_Backend_Assignment
    

2. Build and start the Docker containers using Docker Compose:

    
  Command: docker-compose up --build
   

  //This command builds the Docker images specified in the `Dockerfile` and starts the containers defined in `docker-compose.yml`.

## Step 3: Apply Migrations
1. Open a new terminal window (or use another tab in your current terminal).
2. Navigate to the repository directory:

    
  Command: cd Codemonk_Backend_Assignment
    

3. Apply database migrations to create the necessary tables:

    
  Command: docker-compose run web python manage.py migrate
    

4. Create a superuser account:

    
  Command: docker-compose run web python manage.py createsuperuser
    

    Follow the prompts to enter a username, email, and password for the superuser.


## Step 4: Accessing API Endpoints

### Register a New User
**Endpoint:** `POST /api/register/`  
**Description:** Register a new user.

//Use the following curl command to register a new user:


Command: curl -X POST http://localhost:8000/api/register/ -d "email=user@example.com&password=yourpassword&name=YourName&dob=YYYY-MM-DD"


Example:

Command: curl -X POST http://localhost:8000/api/register/ -d "email=test1@example.com&password=test1&name=test1&dob=1990-10-10"


### Login and Obtain JWT Tokens
**Endpoint:** `POST /api/login/`  
**Description:** Login and obtain JWT tokens.

//Use the following curl command to login:


Command: curl -X POST http://localhost:8000/api/login/ -d "email=user@example.com&password=yourpassword"

Example:

Command: curl -X POST http://localhost:8000/api/login/ -d "email=test1@example.com&password=test1"

//From the response, copy the access token for use in subsequent commands.


### Create a New Paragraph (Authenticated)
**Endpoint:** `POST /api/paragraphs/`  
**Description:** Create a new paragraph.

//Use the following curl command to create a new paragraph (replace `your-access-token` with the actual token obtained from the login step):

Command: curl -X POST -H "Authorization: Bearer your-access-token" http://localhost:8000/api/paragraphs/ -d "text=Your paragraph content"

Example:

Command: curl -X POST -H "Authorization: Bearer your-access-token" http://localhost:8000/api/paragraphs/ -d "text=This is a test paragraph. \n\n How are you?"


### Search Paragraphs by Word (Authenticated)
**Endpoint:** `GET /api/search/?word=`  
**Description:** Search for paragraphs containing a specific word.

//Use the following curl command to search for paragraphs (replace `your-access-token` with the actual token and `search-word` with the word you want to search for):


Command: curl -H "Authorization: Bearer your-access-token" http://localhost:8000/api/search/?word=search-word


## Step 5: Verify Database Entries
To verify the entries in the PostgreSQL database:

1. Access the PostgreSQL database running in the Docker container:

    
   Command: docker-compose exec db psql -U postgres app
    
   // Here, `app` is the name of the database specified in `docker-compose.yml`.

2. Once inside the PostgreSQL prompt, you can query the database tables. For example, to see the users in the database:

    
    Command: SELECT * FROM paragraphs_customuser;
    

## Alternative Way to Check the API Endpoints
You can also use Postman to interact with the API endpoints. Refer to the Postman API documentation for detailed instructions on how to set up and use Postman for testing API endpoints.
