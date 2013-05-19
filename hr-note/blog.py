import jinja2
import os
import webapp2 
from datetime import datetime
from google.appengine.ext import db
from models import Blog


TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja2_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))


class BaseHandler(webapp2.RequestHandler):
    
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)
    
    def render_template(self, template, context, **args):
        t = jinja2_environment.get_template(template)
        self.response.out.write(t.render(context))


class IndexPage(BaseHandler):
    
    def get(self):
        blogs = Blog.all()
        self.render_template('index.html',{
                'blogs':blogs,
                })

class DetailPage(BaseHandler):
    
    def get(self, blog_id):
        blog_id = int(blog_id)
        blog = db.get(db.Key.from_path('Blog', blog_id))
        self.render_template('detail.html',{
                'blog':blog,
                })
        

class CreatePage(BaseHandler):
    
    def get(self):
        self.render_template('new.html')
        
    def Post(self):
        title = self.Request.get('title')
        content = self.Request.get('content')
        
        blog = Blog(title=title,
                    content=content)
        blog.put()
        return webapp2.redirect('/blog')
        

app = webapp2.WSGIApplication([
        ('/blog/', IndexPage),
        ('/blog/detail/([\d]+)', DetailPage),
        ('/blog/create/', CreatePage),
        ],
                              debug=True)
