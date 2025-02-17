import smtplib
from email.mime.text import MIMEText
import firebase_admin
from firebase_admin import credentials, messaging
from config import Config

# Initialize Firebase app
cred = credentials.Certificate(Config.FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred)

def send_email(recipient, subject, message):
    try:
        msg = MIMEText(message, 'html')
        msg['Subject'] = subject
        msg['From'] = Config.SMTP_USERNAME
        msg['To'] = recipient

        with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
            server.starttls()
            server.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
            server.sendmail(Config.SMTP_USERNAME, recipient, msg.as_string())
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

def send_push_notification(recipient_token, message):
    try:
        message = messaging.Message(
            notification=messaging.Notification(
                title='Notification',
                body=message,
            ),
            token=recipient_token,
        )
        response = messaging.send(message)
        print('Successfully sent message:', response)
        return True
    except Exception as e:
        print(f"Failed to send push notification: {e}")
        return False