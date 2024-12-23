from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download-resume")
def download_resume():
    return send_from_directory(directory=".", path="resume.pdf", as_attachment=True)

app.run()
