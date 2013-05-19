#!/usr/bin/env python
#coding=utf8

from google.appengine.ext import db


class Blog(db.Model):
    
    title = db.StringProperty(required=True)
    author = db.StringProperty(default="hackrole")
    content = db.TextProperty(required=True)
    create_time = db.DateProperty(auto_now_add=True)
    is_public = db.BooleanProperty(default=True)
