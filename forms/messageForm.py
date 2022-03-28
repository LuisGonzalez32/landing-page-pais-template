from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


class MessageForm(FlaskForm):
    firstname = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=200),
        ],
        render_kw={"placeholder": "First name"},
    )
    
    lastname = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=200),
        ],
        render_kw={"placeholder": "Last name"},
    )
    
    email = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=200),
        ],
        render_kw={"placeholder": "Email"},
    )
    
    message = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=200),
        ],
        render_kw={"placeholder": "Message"},
    )
    

    submit = SubmitField("Send message")
