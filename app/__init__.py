from flask import Flask
#from flask.ext.sessions import Session
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "hs@50(!vclWa]AxM#b84?-BL(dn3!sT8_dBm6<lA&dU2"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:RSK4LFEg@localhost/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
