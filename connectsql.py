from flask import Flask
import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  String
import config

# DB class
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = 'student'
    studentid = db.Column('studentid', String(20), primary_key=True)
    studentname = db.Column('studentname', String(30), unique=False)
    subject = db.Column('subject', String(50), unique=False)
    college = db.Column('college', String(50), unique=False)

    def __init__(self, studentid=None, studentname=None, subject=None, college=None):
        self.studentid = studentid
        self.studentname = studentname
        self.subject = subject
        self.college = college

    def __repr__(self):
        return '<Student %s>' % (self.studentid) % (self.studentname) % (self.subject) % (self.college)


if __name__ == '__main__':
    db.create_all()
