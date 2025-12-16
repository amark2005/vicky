from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {"title": "Project Alpha", "desc": "A web application built with Flask."},
        {"title": "Project Beta", "desc": "Data analysis tool using Python."},
        {"title": "Project Gamma", "desc": "Mobile app developed in Flutter."}
    ]
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)