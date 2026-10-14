# INF601 - Advanced Programming in Python
# Gabriel Itegbe
# Mini Project 5
import os
from dotenv import load_dotenv
import sqlite3
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv() # This loads the .env file

app = Flask(__name__)
# Grab the key from the .env file, with a fallback just in case
app.secret_key = os.environ.get('SECRET_KEY', 'fallback_super_secret_key')
DATABASE = 'database.db'
# --- Database Helper Functions ---
def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db
def init_db():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    db.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            genre TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    db.commit()
    db.close()

# --- Login Required Decorator ---
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# --- Routes ---

# 1. Home Page
@app.route('/')
def index():
    return render_template('index.html')

# 2. About Page
@app.route('/about')
def about():
    return render_template('about.html')

# 3. Register Page (GET and POST)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db = get_db()
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone() is not None:
            error = f'User {username} is already registered.'
        
        if error is None:
            db.execute(
                'INSERT INTO users (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            db.close()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        
        flash(error, 'danger')
        
    return render_template('register.html')

# 4. Login Page (GET and POST)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'
            
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('watchlist'))
            
        flash(error, 'danger')
        
    return render_template('login.html')

# 5. Watchlist Page (Requires Login, GET and POST with Modal Form)
@app.route('/watchlist', methods=['GET', 'POST'])
@login_required
def watchlist():
    db = get_db()
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        user_id = session['user_id']
        
        if title:
            db.execute('INSERT INTO movies (user_id, title, genre) VALUES (?, ?, ?)',
                       (user_id, title, genre))
            db.commit()
            flash('Movie added to your watchlist!', 'success')
        else:
            flash('Movie title is required.', 'danger')
            
    movies = db.execute(
        'SELECT * FROM movies WHERE user_id = ? ORDER BY id DESC', (session['user_id'],)
    ).fetchall()
    db.close()
    return render_template('watchlist.html', movies=movies)

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db() # Initialize database tables on startup
    app.run(debug=True)