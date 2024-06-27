from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_mail import Message
from app import app, mail

contact_bp = Blueprint('contact_bp', __name__)

@contact_bp.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        question = request.form.get('question')
        file = request.files['file']

        msg = Message('Contact Form Submission', recipients=[email])
        msg.body = f'Name: {name}\nPhone: {phone}\nEmail: {email}\nQuestion: {question}'
        
        if file:
            msg.attach(file.filename, file.content_type, file.read())
        
        mail.send(msg)

        verification_msg = Message('Submission Received', recipients=[email])
        verification_msg.body = 'Thank you for contacting us. We have received your submission.'
        mail.send(verification_msg)

        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact_bp.contact'))

    return render_template('contact.html')
