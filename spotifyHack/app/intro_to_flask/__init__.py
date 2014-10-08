from flask import Flask

app = Flask(__name__)
#WTF_CSRF_ENABLED = True
#SECRET_KEY = 'you-will-never-guess'
app.secret_key = 'development key'
 
#app.config["MAIL_SERVER"] = "smtp.gmail.com"
#pp.config["MAIL_PORT"] = 465
#app.config["MAIL_USE_SSL"] = True
#app.config["MAIL_USERNAME"] = 'contact@example.com'
#app.config["MAIL_PASSWORD"] = 'your-password'
 
#from routes import mail
#mail.init_app(app)
 
import intro_to_flask.routes