from flask import Flask, url_for
from markupsafe import escape
from flask import render_template, request
from utils.email import EmailService

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', )

@app.route('/index.html')
def index_x():
    return render_template('index.html', )

@app.route('/about.html')
def about():
    return render_template('about.html', )


@app.route('/contact.html', methods=["GET", "POST"])
def contact():
    print(app)
    if request.method == "POST":
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        phone = request.form.get("phone", "")
        message = request.form.get("message", "")
        message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
        EmailService(app).send_mail(email, name, message)

    return render_template('contact.html', )

@app.route('/time.html')
def time():
    return render_template('time.html', )

@app.route('/coaching.html')
def coaching():
    return render_template('coaching.html', )

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
