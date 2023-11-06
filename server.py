from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(_name_)

# Configure Flask Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your Gmail address
app.config['MAIL_PASSWORD'] = 'your-password'  # Replace with your Gmail password

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        place = request.form['place']
        pincode = request.form['pincode']
        aadhar = request.form['aadhar']
        age = request.form['age']
        phone = request.form['phone']

        # Compose the email message
        msg = Message('New Student Registration',
                      sender='your-email@gmail.com',  # Replace with your Gmail address
                      recipients=['ammhssedl@gmail.com'])  # Replace with your recipient email address
        msg.body = f"Name: {name}\nAddress: {address}\nPlace: {place}\nPincode: {pincode}\nAadhar: {aadhar}\nAge: {age}\nPhone: {phone}"

        # Send the email
        mail.send(msg)

        return redirect(url_for('index'))

if _name_ == '_main_':
    app.run(debug=True)
