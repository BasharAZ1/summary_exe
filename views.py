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

    bucket_name = 'labkaliedoo19980'
    object_name = f'Israel-1200-BarLev.png'  
    image_url = f'https://{bucket_name}.s3.us-west-2.amazonaws.com/{object_name}'
    return render_template('welcome.html', username=username, image_url=image_url)


def welcome(username):
    bucket_name = 'labkaliedoo19980'
    object_name = 'Israel-1200-BarLev.png'

    session = boto3.Session(
        aws_access_key_id=os.getenv('S3_KEY_ID'),
        aws_secret_access_key=os.getenv('S3_ACCESS_KEY'),
        region_name='us-west-2'
    )


    s3_client = session.client('s3')


    image_url = s3_client.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': bucket_name,
            'Key': object_name
        },
        ExpiresIn=3600 
    )

    return render_template('welcome.html', username=username, image_url=image_url)
