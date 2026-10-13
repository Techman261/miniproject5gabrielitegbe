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