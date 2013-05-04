import cgi
import datetime
import urllib
import webapp2

from google.appengine.ext import db
from google.appengine.api import users


class Greeting(db.Model):
    """
    Modles an individual Guestbook entry with author,
    content and data ...
    """
    author = db.StringProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)
    

def guestbook_key(guestbook_name=None):
    """
    Constructs a Datastore key for a Guestbook entity
    with guestbook_name
    """
    return db.Key.from_path("Guestbook", guestbook_name or  'default_guestbook')


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write("<time>")
        greetings = db.GqlQuery("select * from Greeting where
ANCESTOR is :1 order by date desc limit 30", guestbook_key(Guestbook_name))
        
        for greeting in greetings:
            if greeting.author:
                self.response.write('<b>%s</b>wrote:' % greeting.author)
            else:
                self.response.write('an anoy person write')
                
