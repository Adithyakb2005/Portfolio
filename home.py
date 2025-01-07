from flask import Flask, render_template, send_from_directory, redirect, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view-resume")
def view_resume():
    return send_from_directory(directory="static/images", path="Adithyakb.pdf")

@app.route("/submit-contact", methods=["POST"])
def submit_contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO contacts (name, email, message)
        VALUES (?, ?, ?)
    ''', (name, email, message))
    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/view-contacts")
def view_contacts():
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    conn.close()
    return render_template("contacts.html", contacts=contacts)

if __name__ == "__main__":
    app.run(debug=True)
