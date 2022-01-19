from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    project_title = db.Column('Project Title', db.String())
    completion_date = db.Column('Completion Date', db.DateTime())
    description = db.Column('Description', db.Text())
    skills = db.Column('Skills', db.Text())
    url = db.Column('URL', db.Text())


def __repr__(self):
    return f'''<Project (Project Title: {self.project_title}
            Completion Date: {self.completion_date}
            Description: {self.description}
            Skills: {self.skills}
            URL: {self.url})
            '''