from intro_to_flask import app
from flask import render_template, request, flash
from forms import SearchForm
#from flask.ext.mail import Message, Mail
 
app = Flask(__name__) 
 
app.secret_key = 'development key'

@app.route('/')
def home():
  return render_template('home.html')



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