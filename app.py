from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

app.route('/')
def home():
    return render_template('testinggit.html')

if __name__ == '__main__':
    app.run()