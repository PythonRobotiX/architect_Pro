from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app as app
import openai
from flask_mail import Message
from backend import mail

thesis_bp = Blueprint('thesis_bp', __name__)

@thesis_bp.route('/create_smart_thesis', methods=['GET', 'POST'])
def create_smart_thesis():
    if request.method == 'POST':
        description = request.form.get('description')
        # Call OpenAI API with the description
        openai.api_key = app.config['OPENAI_API_KEY']
        response = openai.Completion.create(
            engine="davinci",
            prompt=description,
            max_tokens=1024
        )
        thesis_content = response.choices[0].text
        return thesis_content
    return render_template('smart_thesis.html')

@thesis_bp.route('/email_smart_thesis', methods=['POST'])
def email_smart_thesis():
    description = request.form.get('description')
    # Call OpenAI API with the description
    openai.api_key = app.config['OPENAI_API_KEY']
    response = openai.Completion.create(
        engine="davinci",
        prompt=description,
        max_tokens=1024
    )
    thesis_content = response.choices[0].text

    email = request.form.get('email')
    msg = Message('Your Smart Thesis', recipients=[email])
    msg.body = thesis_content
    mail.send(msg)
    return "Email sent successfully!"
