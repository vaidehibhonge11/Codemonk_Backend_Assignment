Paragraph API Setup Guide

#Prerequisites
Before you begin, make sure you have the following installed on your system:
1. Docker
2. Git

#Step 1: Clone the Repository
Open your terminal (Command Prompt, PowerShell, or Terminal).
Clone the repository using Git:

git clone https://github.com/vaidehibhonge11/Codemonk_Backend_Assignment
cd <repository-directory>


#Step 2: Build and Start Docker Containers
Navigate into the cloned repository directory:

cd <repository-directory>
Build and start the Docker containers using Docker Compose:

docker-compose up --build
This command builds the Docker images specified in Dockerfile and starts the containers defined in docker-compose.yml.

#Step 3: Apply Migrations
Open a new terminal window (or use another tab in your current terminal).
Navigate to the repository directory:

cd <repository-directory>
Apply database migrations to create necessary tables:

docker-compose run web python manage.py migrate

Follow the prompts to enter a username, email, and password for the superuser.

#Step 4: Accessing API Endpoints
Register a New User
Endpoint: POST /api/register/
Description: Register a new user.

curl -X POST http://localhost:8000/api/register/ -d "email=user@example.com&password=yourpassword&name=YourName&DOB=YYYY-MM-DD"
eg:curl -X POST http://localhost:8000/api/register/ -d "email=test1@example.com&password=test1&name=test1&dob=1990-10-10"


Login and Obtain JWT Tokens
Endpoint: POST /api/login/
Description: Login and obtain JWT tokens.

curl -X POST http://localhost:8000/api/login/ -d "email=user@example.com&password=yourpassword"
(from the response of this command copy the access token and use it next commands)
eg: curl -X POST http://localhost:8000/api/login/ -d "email=test1@example.com&password=test1"


Create a New Paragraph (Authenticated)
Endpoint: POST /api/paragraphs/
Description: Create a new paragraph.

curl -X POST -H "Authorization: Bearer <your-access-token>" http://localhost:8000/api/paragraphs/ -d "content=Your paragraph content"
eg: curl -X POST -H "Authorization: Bearer (Your access token received from previous command)" http://localhost:8000/api/paragraphs/ -d "text=This is test paragraph1. \n\n how are you"


Search Paragraphs by Word (Authenticated)
Endpoint: GET /api/search/?word=<word>
Description: Search for paragraphs containing a specific word.(Replace the word to be searched in place of 'search-word')

curl -H "Authorization: Bearer <your-access-token>" http://localhost:8000/api/search/?word=search-word


#Step 5: Verify Database Entries
Access the PostgreSQL database running in the Docker container:

docker-compose exec db psql -U postgres app

Here, app is the name of the database specified in docker-compose.yml.
Once inside the PostgreSQL prompt, you can query database tables to verify entries:


SELECT * FROM paragraphs_customuser;
(From above query you should be able to see the users of paragraphs in the database.)

ALTERNATIVE WAY TO CHECK THE API ENDPOINTS FOLLOW THE POSTMAN API DOCUMENTATION.
