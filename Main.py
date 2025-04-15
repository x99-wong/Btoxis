import os
from twilio.rest import Client
from flask import Flask, request

app = Flask(__name__)

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")  # e.g., 'whatsapp:+14155238886'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route("/whatsapp", methods=['POST'])
def reply_whatsapp():
    message_body = request.form['Body']
    sender = request.form['From']

    if "hello" in message_body.lower():
        response = "Hello there! How can I help you?"
    else:
        response = "Sorry, I didn't get that. Try saying 'hello'."

    client.messages.create(
        body=response,
        from_=TWILIO_PHONE_NUMBER,
        to=sender
    )

    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
