from flask import Flask, request, jsonify
from notification import send_email, send_push_notification

app = Flask(__name__)

@app.route('/notify/email', methods=['POST'])
def notify_email():
    data = request.get_json()
    recipient = data.get('recipient')
    subject = data.get('subject')
    message = data.get('message')
    if send_email(recipient, subject, message):
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'failure'}), 500

@app.route('/notify/push', methods=['POST'])
def notify_push():
    data = request.get_json()
    recipient_token = data.get('recipient_token')
    message = data.get('message')
    if send_push_notification(recipient_token, message):
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'failure'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)