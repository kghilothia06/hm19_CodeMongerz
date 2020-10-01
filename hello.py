from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, GetMedicineForm
app = Flask(__name__)#for user interface

app.config['SECRET_KEY'] = '9de51b03208ed35d21fadfc384be03e1'

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
   form = GetMedicineForm()
   if form.validate_on_submit():
      flash(f'Prescription is finally uploaded for {form.firstname.data}' , 'success')
      return redirect(url_for('home'))
   return render_template('home.html',title='', form=form)

@app.route('/about')
def about():
   return render_template('about.html', title='About') 

@app.route('/register', methods=['GET','POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
      flash(f'Account created for {form.username.data}!', 'success')
      return redirect(url_for('home'))
   return render_template('register.html',title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
      if form.email.data == 'admin@medex.com' and form.password.data == 'aayush':
         flash(f'You have been logged in as {form.email.data}!', 'success')
         return redirect(url_for('home'))
      else :
         flash('Login Unsuccessful. Please check username and password', 'danger')
   return render_template('login.html',title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
