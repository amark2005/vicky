from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {"title": "Project money", "desc": ""},
        {"title": "Project Dress shop", "desc": ""},
        {"title": "Project Loosu-Bunda", "desc": ""}
    ]
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
