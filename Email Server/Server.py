from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        sender_email = 'prateekya23@gmail.com'  # Your email address
        # sender_password = 'PrateeK12@'      # Your email password
        sender_password = 'pgzvrlgnpjjouxcs'      # Your email password

        receiver_email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Set up the SMTP server
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(sender_email, sender_password)

        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach the message to the email
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        smtp_server.send_message(msg)

        # Close the SMTP server
        smtp_server.quit()

        return 'Email sent successfully!'
    else:
        return 'Method Not Allowed'

if __name__ == '__main__':
    app.run(debug=True)
