from flask_mail import Message
from app import mail, app
from flask import render_template
from threading import Thread

# Sends the email inside an app context since this runs in a background thread.
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

# Builds and dispatches an email, firing it off in a thread so the request doesn't block.
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)
    Thread(target=send_async_email, args=(app, msg)).start()

# Generates a reset token and emails both the plain-text and HTML versions to the user.
def send_password_request_email(user):
    token = user.get_reset_password_token()
    send_email(
        '[Microblog] Reset Your Password',
        sender=app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('email/reset_password.txt',
                                  user=user, token=token),
        html_body=render_template('email/reset_password.html',
                                  user=user, token=token)
    )
