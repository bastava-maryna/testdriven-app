import os, sys, datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app = Flask(__name__)

# set config
#app.config.from_object('project.config.DevelopmentConfig')

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# to check that correct config chosen
# comment after checking
print(app.config, file=sys.stderr)

# instantiate the db
db = SQLAlchemy(app)

# model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })