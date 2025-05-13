from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/programs')
def programs():
    return render_template('programs.html')

@main.route('/get-involved')
def get_involved():
    return render_template('get-involved.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # You can add logic to send email or store messages
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Received message from {name} ({email}): {message}")
    return render_template('contact.html')