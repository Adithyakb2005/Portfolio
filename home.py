from flask import Flask,render_template
# import sqlite3
app=Flask(__name__)
# conn = sqlite3.connect('database.db')
# try:
#     conn.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age INTEGER)''')
# except:
#     pass

# Home route
@app.route('/')
def home():
    return render_template('index.html')

app.run()