from intro_to_flask import app
from flask import request,render_template,flash,redirect
from forms import SearchForm,LoginForm
from userauth import userauth
#from flask.ext.mail import Message, Mail
 


@app.route('/', methods=['GET', 'POST'])
def home():
  #form = LoginForm(); 
  #username = form.openid;
  #user_playlists_contents.user_playlists_contents(username);
  if request.method == 'POST':
    if request.form['submit'] == 'Login with Spotify':
      userauth()
    else:
      pass # unknown
  elif request.method == 'GET':
    userauth()
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In',form=form)


@app.route("/find_list", methods=['GET', 'POST'])
def find_list():
  form = SearchForm()
  if request.method == 'POST':
    return 'Form posted.'
  elif request.method == 'GET':
  	return render_template('find_list.html', form=form)

@app.route('/about')
def about():
  return render_template('about.html')

#@app.route('/search')
#def searchRoom():
 
 
#if __name__ == '__main__':
  #app.run(debug=True)