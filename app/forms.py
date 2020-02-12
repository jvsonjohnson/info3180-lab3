from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField("", validators=[DataRequired()])
    email = StringField("", validators=[DataRequired(), Email()])
    subject = StringField("", validators=[DataRequired()])
    message = StringField("", validators=[DataRequired()])

