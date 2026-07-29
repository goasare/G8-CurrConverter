import os
from flask import Flask, render_template, url_for, flash, redirect
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

from forms import RegistrationForm
from models import db, User

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  #os.getenv('DATABASE_URL')

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", methods=['GET', 'POST'])
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)

        if form.country.data == 'OTHER':
            user_currency = None
        else:
            user_currency = form.country.data
        
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, currency=user_currency)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}.', 'success')
        return redirect(url_for('converter'))
    
    return render_template('register.html', title='Register', form=form)

@app.route("/converter")
def converter():
    return "<p> Converter page coming soon! </p>"

if __name__ == '__main__':
    app.run(debug=True)