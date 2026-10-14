# Mini Project 5 - Flask Web App

# INF601 - Advanced Programming in Python

**Name:** Gabriel Itegbe
**Repository:** miniproject5GabrielItegbe

## Project Overview
This project is a Flask-based web application called *Movie Watchlist*. It allows users to register for an account, log in securely, and maintain a personal list of movies they want to watch. The application demonstrates core web development concepts including routing, session management, database integration with relational tables, and responsive UI design using Bootstrap.

## Project Structure
The application follows the standard Flask folder structure required for this project:

text
miniproject5GabrielItegbe/
│── app.py                 # Main Flask application, database setup, and routes
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
│── templates/             # HTML templates
│   │── base.html          # Base layout with Bootstrap and Navbar
│   │── index.html         # Home page
│   │── about.html         # About page
│   │── register.html      # Registration form (GET/POST)
│   │── login.html         # Login form (GET/POST)
│   └── watchlist.html     # Protected watchlist page with Bootstrap Modal


## How to Install Requirements
To run this project, you need Python installed on your machine. Follow these steps to set up your local environment:

1. *Clone the repository* and navigate into the project folder:
   bash
   git clone https://github.com/your-username/miniproject5GabrielItegbe.git
   cd miniproject5GabrielItegbe
   
2. *Create a virtual environment* to keep dependencies isolated:
   bash
   # Windows
   python -m venv venv
   
   # Mac/Linux
   python3 -m venv venv
   
3. *Activate the virtual environment*:
   bash
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   
   (You will know it is activated when you see (venv) at the start of your terminal prompt).
4. *Install the required packages* using the requirements.txt file:
   bash
   pip install -r requirements.txt
   

## How to Initialize the Database
This project uses a SQLite database (database.db) with two tables (users and movies) linked by a foreign key. 

*You do not need to run any manual SQL scripts.* The database and its tables are initialized automatically the very first time you run the application. When you start the server, the init_db() function at the bottom of app.py checks if the database exists and creates the necessary tables if they do not.

## How to Run the Development Server
Once your virtual environment is activated and the dependencies are installed, you can start the Flask development server:

1. Ensure your terminal is in the root directory of the project (where app.py is located).
2. Run the following command:
   bash
   python app.py
   
3. Open your web browser and navigate to the local URL provided in the terminal output (usually *http://127.0.0.1:5000* or *http://localhost:5000*).
4. You can now register a new user, log in, and start adding movies to your watchlist!

---

## AI Usage

*What AI Provided:*
I used AI to help structure the initial Flask boilerplate, generate the SQLite schema with the required foreign key relationship, and write the Bootstrap HTML templates. Specifically, I asked the AI to include a Bootstrap modal for the "Add Movie" form and to ensure the code followed standard Flask tutorial patterns for session-based authentication and GET/POST routing.

*Changes I Made:*
While the AI provided a strong foundation, I reviewed, tested, and modified the generated code to ensure it met the specific grading rubric requirements for Mini Project 5. I manually adjusted the folder structure, customized the Bootstrap styling to fit the "Movie Watchlist" theme, and ensured all routes properly handled edge cases (like duplicate usernames during registration). I also manually managed my Git commits to ensure I met the requirement of at least 5 distinct commits.