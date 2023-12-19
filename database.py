from flask import Flask, request, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
# import sqlite3
import os

current = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.secret_key = '12345'
app.config['SECRET_KEY'] = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current,"project.sqlite3")
db = SQLAlchemy(app)
api = Api(app)
app.app_context().push()


class District(db.Model):
    name = db.Column(db.String(55), primary_key=True)
    state = db.Column(db.String(55))

class Experience(db.Model):
    name = db.Column(db.String(55), primary_key=True)

class JobPreference(db.Model):
    preference_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    job_type = db.Column(db.String(50))
    location = db.Column(db.String(100))
    industry = db.Column(db.String(50))

class JobType(db.Model):
    name = db.Column(db.String(50), primary_key=True)

class JobsForWomen(db.Model):
    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_title = db.Column(db.String(255))
    job_description = db.Column(db.Text)
    is_active = db.Column(db.Boolean)
    created_on = db.Column(db.Date)
    job_type = db.Column(db.String(50))
    qualification = db.Column(db.String(50))
    experience = db.Column(db.String(50))
    location = db.Column(db.String(50))

class Jobs(db.Model):
    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_title = db.Column(db.String(255))
    job_description = db.Column(db.Text)
    is_active = db.Column(db.Boolean)
    created_on = db.Column(db.Date)
    job_type = db.Column(db.String(50))
    qualification = db.Column(db.String(50))
    experience = db.Column(db.String(50))
    location = db.Column(db.String(50))

class Qualification(db.Model):
    name = db.Column(db.String(55), primary_key=True)

class Skills(db.Model):
    skill_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    skill_name = db.Column(db.String(255))
    description = db.Column(db.Text)

class State(db.Model):
    name = db.Column(db.String(55), primary_key=True)

class UserHistory(db.Model):
    history_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    job_viewed = db.Column(db.Integer)
    course_taken = db.Column(db.Integer)
    counselling_attended = db.Column(db.Integer)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

class Counselling(db.Model):
    counselling_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(255))
    description = db.Column(db.Text)

# def execute_sql_scripts(sql_files, database_path):
#     # Connect to SQLite database
#     conn = sqlite3.connect(database_path)
#     cursor = conn.cursor()

#     for sql_file in sql_files:
#         # Read and execute SQL commands from the file
#         with open(sql_file, 'r') as file:
#             sql_script = file.read()
#             cursor.executescript(sql_script)

#     # Commit the changes and close the connection
#     conn.commit()
#     conn.close()

# if __name__ == '__main__':
#     # Replace the list with the actual paths to your SQL files
#     sql_files = ['chatbot_counselling.sql', 'chatbot_district.sql','chatbot_experience.sql','chatbot_job_preference.sql','chatbot_job_type.sql','chatbot_jobs_for_women.sql','chatbot_jobs.sql','chatbot_qualification.sql','chatbot_skills.sql','chatbot_state.sql','chatbot_user_history.sql','chatbot_user.sql']

#     # Replace 'your_database_name.sqlite3' with the name of your SQLite database
#     database_path = 'project.sqlite3'

#     # Execute the SQL scripts
#     execute_sql_scripts(sql_files, database_path)

#     # The rest of your Flask code here
#     # ...

#     # Run the Flask app
#     app.run(debug=True)
