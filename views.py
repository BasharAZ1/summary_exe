from flask import render_template, request, redirect, flash, url_for
from models import User, db
import boto3
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
    bucket_name = 'labkaliedoo19980'
    object_name = 'Israel-1200-BarLev.png'
    region = 'us-west-2'
    s3 = boto3.client('s3')

    try:
        image_url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': object_name}, ExpiresIn=3600)
    except Exception as e:
        return f"Error generating presigned URL: {str(e)}", 500

    return render_template('welcome.html', username=username, image_url=image_url)
