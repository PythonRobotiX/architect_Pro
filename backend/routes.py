from flask import render_template, request, jsonify
from backend import db, mail
from flask_mail import Message
from backend import create_app
from sqlalchemy import text

app = create_app()

# Sample data for demonstration
projects = [
    {
        "id": 1,
        "name": "Project Name 1",
        "year": 2021,
        "files": [
            {"type": "video", "url": "project1-1.mp4"},
            {"type": "video", "url": "project1-2.mpeg"},
            {"type": "video", "url": "project1-3.mov"},
            {"type": "document", "url": "project1-4.pdf"},
            {"type": "image", "url": "project1-5.jpg"},
            {"type": "image", "url": "project1-6.jpeg"},
            {"type": "image", "url": "project1-7.png"},
        ]
    },
    # Add more projects as needed
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects', methods=['GET'])
def get_projects():
    return jsonify({"projects": projects})

@app.route('/test-db', methods=['GET'])
def test_db():
    try:
        result = db.session.execute(text('SELECT 1'))
        return jsonify({"message": "Database connected successfully!", "result": [row[0] for row in result]}), 200
    except Exception as e:
        return jsonify({"message": "Database connection failed!", "error": str(e)}), 500

@app.route('/contact', methods=['POST'])
def contact():
    data = request.form
    print("Contact form data received:", data)
    
    # Send verification email
    msg = Message('Contact Form Submission', recipients=[data['email']])
    msg.body = f"Thank you for contacting us, {data['name']}.\n\nWe have received your message and will get back to you shortly."
    mail.send(msg)
    
    return jsonify({"message": "Contact form submitted successfully"}), 201

@app.route('/healthz', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200
