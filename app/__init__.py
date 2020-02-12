from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
app.config["SECRET_KEY"] = "staywoke"
app.config["MAIL_SERVER"] = "smtp.mailtrap.io"
app.config["MAIL_PORT"] = "465"  # (or try 2525)
app.config["MAIL_USERNAME"] = "3ec7d02ea242c8"
app.config["MAIL_PASSWORD"] = "731e330948a3d0"

mail = Mail(app)
from app import views

