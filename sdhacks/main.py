import webapp2
import os
import jinja2

from google.appengine.ext import ndb
from google.appengine.api import users
#add users api

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #loads the home page
        current_user = users.get_current_user()
        logout_url = users.create_logout_url('/')
        login_url = users.create_login_url('/')

        template_vars = {
            "current_user": current_user,
            "logout_url": logout_url,
            "login_url": login_url,
        }
        template = jinja_environment.get_template("templates/home.html")
        self.response.write(template.render(template_vars))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/about.html")
        self.response.write(template.render())
        
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about', AboutHandler)
], debug=True)
