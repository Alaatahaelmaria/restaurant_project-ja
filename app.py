from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # ضروري عشان الرسائل

# Connect to SQL (SQLite)
def sql_connection():
    conn = sqlite3.connect('users.db')
    return conn

# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['restaurant_db']
restaurant_collection = mongo_db['restaurants']


# Home Page (Login Page)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sql_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            return redirect(url_for('search'))
        else:
            flash('Invalid username or password!', 'error')

    return render_template('login.html')


# Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sql_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except:
            flash('Registration failed. Username might already exist.', 'error')
        finally:
            conn.close()

    return render_template('register.html')


# Search Restaurants
@app.route('/search', methods=['GET', 'POST'])
def search():
    results = []
    if request.method == 'POST':
        search_criteria = {}

        if request.form.get('name'):
            search_criteria['name'] = {'$regex': request.form.get('name'), '$options': 'i'}

        if request.form.get('street'):
            search_criteria['street'] = {'$regex': request.form.get('street'), '$options': 'i'}

        if request.form.get('borough'):
            search_criteria['borough'] = {'$regex': request.form.get('borough'), '$options': 'i'}

        if request.form.get('cuisine'):
            search_criteria['cuisine'] = {'$regex': request.form.get('cuisine'), '$options': 'i'}

        if request.form.get('grade'):
            search_criteria['grade'] = request.form.get('grade')

        results = list(restaurant_collection.find(search_criteria))

    return render_template('search.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
