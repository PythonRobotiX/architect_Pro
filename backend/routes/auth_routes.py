from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_mail import Message
from app import app, db, mail
from models import User
import random

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        captcha = request.form.get('captcha')

        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('auth_bp.create_account'))

        verification_code = random.randint(100000, 999999)
        session['verification_code'] = verification_code

        user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        msg = Message('Email Verification', recipients=[email])
        msg.body = f'Your verification code is {verification_code}'
        mail.send(msg)

        return redirect(url_for('auth_bp.verify_email'))
    
    return render_template('create_account.html')

@auth_bp.route('/verify_email', methods=['GET', 'POST'])
def verify_email():
    if request.method == 'POST':
        code = request.form.get('verification_code')
        if code == session.get('verification_code'):
            flash('Congratulations! You created your account successfully! Please go back to the home page and login.', 'success')
            return redirect(url_for('auth_bp.login'))
        else:
            flash('Verification code is incorrect!', 'danger')
    
    return render_template('verify_email.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials!', 'danger')

    return render_template('login.html')
