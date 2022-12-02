import smtplib
import ssl
import os
from dotenv import load_dotenv
from email.message import EmailMessage

TAG = "ECE Ordering"
SUPER_USER = os.environ.get("SUPER_USER_EMAIL")
BASE_URL = os.environ.get("BASE_URL")

def send_order_email(order_id, vendor, order_url, creator):
    subject = f"[{TAG}] New Order Received"
    receiver = SUPER_USER
    message = f"""\
Dear Admin,

A new order (Order {order_id} for Vendor {vendor}) was created by {creator.name} ({creator.email}).

The order can be viewed at following URL: {BASE_URL + order_url}

ECE Ordering System
"""
    send_email(subject, receiver, message)

def send_email(subject, receiver, message):
    sender = os.environ.get('SENDER_EMAIL')
    password = os.environ.get('SENDER_PASSWORD')
    context = ssl.create_default_context()
    
    email = EmailMessage()
    email["Subject"] = subject
    email["From"] = sender
    email["To"] = receiver
    email.set_content(message)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.send_message(email)