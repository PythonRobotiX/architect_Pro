from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import openai

portfolio_bp = Blueprint('portfolio_bp', __name__)

@portfolio_bp.route('/show', methods=['GET'])
def show_portfolio():
    return render_template('portfolio.html')

@portfolio_bp.route('/create_smart_portfolio', methods=['GET', 'POST'])
def create_smart_portfolio():
    if request.method == 'POST':
        description = request.form.get('description')
        # Call OpenAI API with the description
        openai.api_key = app.config['OPENAI_API_KEY']
        response = openai.Completion.create(
            engine="davinci",
            prompt=description,
            max_tokens=1024
        )
        portfolio_content = response.choices[0].text
        return portfolio_content
    return render_template('smart_portfolio.html')

@portfolio_bp.route('/email_smart_portfolio', methods=['POST'])
def email_smart_portfolio():
    description = request.form.get('description')
    # Call OpenAI API with the description
    openai.api_key = app.config['OPENAI_API_KEY']
    response = openai.Completion.create(
        engine="davinci",
        prompt=description,
        max_tokens=1024
    )
    portfolio_content = response.choices[0].text

    email = request.form.get('email')
    msg = Message('Your Smart Portfolio', recipients=[email])
    msg.body = portfolio_content
    mail.send(msg)
    return "Email sent successfully!"
