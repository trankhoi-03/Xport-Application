import sqlite3
import smtplib
import string
import random
import re

def get_database_connection():
    db = sqlite3.connect('Database.db')
    cursor = db.cursor()
    return db, cursor

def close_database_connection(db):
    if db:
        db.close()

def toggle_password(signin_password, show_password):
    if show_password.get():
        signin_password.configure(show="")
    else:
        signin_password.configure(show="*")

def check_signin(username, password):
    db, cursor = get_database_connection()
    try:
        cursor.execute("SELECT username, password FROM Users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()

        #If a matching record is found, return True as a succesfull sign in
        if result:
            return True
    except sqlite3.Error as e:
        print("Sqlite error:", e)
    finally:
        close_database_connection(db)

    return False

def signup_user(username, password):
    db, cursor = get_database_connection()
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                username TEXT,
                password TEXT,
                sign_up_date CURRENT_TIMESTAMP
            )   
        ''')
        #Inser data into Users table
        cursor.execute('''
            INSERT INTO Users (username, password) 
            VALUES (?, ?)
        ''', (username, password.lower()))
        db.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    
    finally:
        close_database_connection(db)

def is_valid_characters(input_string):
    #Allow only English letters and standard characters
    pattern = re.compile(r'^[a-zA-Z0-9_\-]+$')
    return pattern.match(input_string) is not None

def is_valid_characters_space(input_string):
    #Allow only English letters, standard characters and spaces
    pattern = re.compile(r'^[a-zA-Z0-9_\- ]+$')
    return pattern.match(input_string) is not None
