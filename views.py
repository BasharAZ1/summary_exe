from flask import render_template, request, redirect, flash, url_for
from models import User, db
from sqlalchemy.exc import IntegrityError

def homepage():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_user = User(username=username, email=email)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('welcome', username=username))   
        except IntegrityError:
            db.session.rollback()
            flash('This username or email is already taken. Please choose a different one.')
            return render_template('index.html')
    return render_template('index.html')

def welcome(username):
    return render_template('welcome.html', username=username)
