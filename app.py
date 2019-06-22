#!/usr/bin/env python3
import os
from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from resources.blog import Blog, BlogList
from flask_cors import CORS

app = Flask(__name__, template_folder='./templates',static_folder='./static')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "tahir"
api = Api(app)

CORS(app) 
@app.route('/')
def index():
    return render_template('index.html')

from db import db
db.init_app(app)
@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Blog, '/blog/<int:id>', '/blog')
api.add_resource(BlogList, '/blogs')

if __name__ == '__main__':

    app.run(port=process.env.PORT, debug=True)
