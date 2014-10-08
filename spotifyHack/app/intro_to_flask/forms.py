from wtforms  import Form, TextField, TextAreaField, SubmitField,PasswordField,StringField,BooleanField
from wtforms.validators import DataRequired

class SearchForm(Form):
  list = TextField("List")
  password = PasswordField("Password")
  submit = SubmitField("Send")

class LoginForm(Form):
    openid = StringField('spotifyid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)