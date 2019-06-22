import sqlite3
from db import db
import json
import base64

class BlogModel(db.Model):
    __tablename__ = "blogs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    content = db.Column(db.String(1000))
    img_name = db.Column(db.String(60))
    img_url = db.Column(db.String(100))

    def __init__(self, title, content, img_name, img_url):
        self.title = title
        self.content = content
        self.img_name = img_name
        self.img_url = img_url
    
    def json(self):
        data = {
            "id":self.id,
            "title":self.title,
            "content":self.content,
            "img_name":self.img_name,
            "img_url":self.img_url
        }
        return data
        
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first() 

    def insert_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

