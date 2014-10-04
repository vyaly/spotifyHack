from wtforms  import Form, TextField, TextAreaField, SubmitField,PasswordField
 
class SearchForm(Form):
  list = TextField("List")
  password = PasswordField("Password")
  submit = SubmitField("Send")
