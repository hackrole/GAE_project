#!/use/bin/env python

import webapp2
import cgi
import datetime
import urllib
from google.appengine.ext import db

class Blog(db.Model):
    b_title = db.StringProperty(required=True)
    b_content = db.TextProperty(required=True)
    b_date = db.DateTimeProperty(auto_now_add=True)

class BlogPage(webapp2.RequestHandler):

    def get(self):
        """
        the blog index page
        """
        blogs = Blog.all().fetch(20)
        l = len(blogs)
        print blogs
        print l
        self.response.write("the blogs length is %s")

class BlogSave(webapp2.RequestHandler):

    def get(self):
        """
        the blog create page
        """
        blog = Blog(b_title="try", b_content="it's the first try for gae blog")
        blog.put()
        self.response.write("new blog create success")
        blogs = Blog.all()
        print blogs
        l = len(blogs.fetch(20))
        self.response.write("the blog lengths is %s" % l)

class MainPage(webapp2.RequestHandler):

    def get(self):
        """
        show hello world! only for test.
        """
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, world!')


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/index', Blog),
    ('/new', BlogSave),
    ], debug=True)

def main():
    url_conf = [
        ('/', MainPage),
        ('/index', Blog),
        ('/new', BlogSave),
        ]
    app = webapp2.WSGIApplication(url_conf, debug=True)
    
