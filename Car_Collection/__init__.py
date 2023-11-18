from flask import Flask 
from flask_migrate import Migrate 


#internal imports 
from .blueprints.site.routes import site 
from .blueprints.auth.routes import auth # <-- ADD THIS
from config import Config 
from .models import login_manager, db 

#instantiating our Flask app
app = Flask(__name__) #passing in the __name__ variable which just takes the name of the folder we're in
app.config.from_object(Config)


#wrap our app in login_manager so we can use it wherever in our app
login_manager.init_app(app)
login_manager.login_view = 'auth.sign_in'
login_manager.login_message = "Hey you! Log in please!"
login_manager.login_message_category = 'warning'



# @app.route("/")
# def Car_Collection():
#     return "<p>Aston Martin Collection</p>"


app.register_blueprint(site)
app.register_blueprint(auth) 



db.init_app(app)
migrate = Migrate(app, db)