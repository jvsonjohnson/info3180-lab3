from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
app.config["SECRET_KEY"] = "staywoke"
app.config["MAIL_SERVER"] = "smtp.mailtrap.io"
app.config["MAIL_PORT"] = 2525
app.config["MAIL_USERNAME"] = "3ec7d02ea242c8"
app.config["MAIL_PASSWORD"] = "731e330948a3d0"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False

mail = Mail(app)
from app import views

