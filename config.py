#this is our configuration file to configure flask to our app location & variables needed to run Flask


from datetime import timedelta
import os #operating system 
from dotenv import load_dotenv #allows us to load our environment variables (variables needed to run application)


# establish our base directory so whenever we use "." to reference any location in our app it knows we are referncing
# rangers_shop folder 
basedir = os.path.abspath(os.path.dirname(__file__))


#need to establish where our environment variables are coming from (this file will be hidden from github)
load_dotenv(os.path.join(basedir, '.env'))



#create our Config class 
class Config():


    FLASK_APP = os.environ.get('FLASK_APP') #looking for key of FLASK_APP in our environment vaariable location (.env)
    FLASK_ENV = os.environ.get('FLASK_ENV') 
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Correct me if Im wrong but Im guessing this can be whatever we want'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #we dont want a message every single time our database is changed
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)