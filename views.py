from flask import render_template, request, redirect, flash, url_for
from models import User, db
from sqlalchemy.exc import IntegrityError
import os
import boto3



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

    bucket_name = os.getenv('S3_BUCKET')
    object_name = f'Israel-1200-BarLev.png '  
    image_url = f'https://{bucket_name}.s3.us-west-2.amazonaws.com/{object_name}'
    return render_template('welcome.html', username=username, image_url=image_url)


