from flask import render_template, request, redirect, flash, url_for,send_file
from models import User, db
from sqlalchemy.exc import IntegrityError
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from io import BytesIO



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

    s3 = boto3.client('s3', region_name=region)
    try:
        s3_response = s3.get_object(Bucket=bucket_name, Key=object_name)
        image_data = s3_response['Body'].read()
        return send_file(BytesIO(image_data), download_name='image.png', mimetype='image/png')
    except (NoCredentialsError, PartialCredentialsError):
        return "Error retrieving the object due to credential issues", 500
    except Exception as e:
        return f"Error retrieving the object: {str(e)}", 500
