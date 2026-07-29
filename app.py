import os
from flask import Flask, render_template, url_for, flash, redirect, request
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from currency import get_liveData, convert_curr

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

CURRENCIES = ['GHS', 'USD', 'EUR', 'JPY', 'GBP', 'NGN', 'DOP', 'CAD', 'CHF', 'ZAR']

@app.route("/converter", methods=['GET', 'POST'])
def converter():
    result = None
    error = None

    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']

        data = get_liveData()
        converted = convert_curr(amount, from_currency, to_currency, data)

        if converted is None:
            error = "Sorry, conversion rate is not available for the selected currencies."
        else:
            result = {
                'amount' : amount,
                'from': from_currency,
                'to': to_currency,
                'converted': converted
            }
    return render_template('converter.html', title='Currency Converter', currencies=CURRENCIES, result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)