import webapp2
import os
import jinja2
#from twilio.rest import Client

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

class FormHandler(webapp2.RequestHandler):
    def get(self):
        #load the form page
        template = jinja_environment.get_template("templates/form.html")
        self.response.write(template.render())

    def post(self):
        phone = self.request.get('phone')
        quote = self.request.get('quote')
        image = self.request.get('img')
        url = None
        if image == "1":
            url = "http://1.bp.blogspot.com/-ZUgbh5Q9Gso/VdMmdjBTJ7I/AAAAAAAACkM/izIcNXoTcb4/s1600/short%2Binspirational%2Bquotes.JPG"
        elif image == "2":
            url = "http://firstdescents.org/wp-content/uploads/2014/01/inspirational-photo.jpg"
        elif image == "3":
            url = "https://i.ytimg.com/vi/FZk40J_drws/maxresdefault.jpg"
        elif image == "4":
            url = "http://photos1.blogger.com/blogger/4614/1851/1600/Tomando_el_sol_1280.jpg"

        account_sid = "ACdef508d68369a117ef857740bf362603"
        auth_token = "96e589688a8b066654d718a105170a44"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            "+" + phone,
            body= quote,
            from_="+14159004260",
            media_url=url
        )
        self.redirect('/results')
        template = jinja_environment.get_template("templates/form.html")
        self.response.write(template.render())

class ResultsHandler(webapp2.RequestHandler):
    def get(self):
        
    #
    #     result_vars = {
    #         'artist' :self.request.get('artist'),
    #         'region' : self.request.get('region'),
    #         'search_response' : search_response,
    #         'vidId':vid_id,
    #         'title':title,
    #         'genre':genre,
    #         'genre1':genre1,
    #         'genre_list':genre_list
    #
    #
    #         #'videos':videos
    #
    #     }
    #     template = jinja_environment.get_template("templates/home.html")
    #     self.response.write(template.render(result_vars))
    # def get(self):
        template = jinja_environment.get_template("templates/result.html")
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about', AboutHandler),
    ('/form', FormHandler),
    ('/results', ResultsHandler)
], debug=True)
