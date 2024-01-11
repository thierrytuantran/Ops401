import smtplib
from email.mime.text import MIMEText
import socket
import time
from datetime import datetime

def send_notification(sender_email, password, receiver_email, host, previous_status, current_status):
    msg = MIMEText(f"Status change for {host}:\nPrevious Status: {previous_status}\nCurrent Status: {current_status}\nTimestamp: {datetime.now()}")
    msg['Subject'] = f"Status Update for {host}"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()

def check_host(host):
    try:
        socket.create_connection((host, 80), timeout=5)
        return "up"
    except socket.error:
        return "down"

def monitor_host(host, sender_email, password, receiver_email):
    last_status = "unknown"
    while True:
        current_status = check_host(host)
        if current_status != last_status:
            send_notification(sender_email, password, receiver_email, host, last_status, current_status)
            last_status = current_status
        time.sleep(60)

# User inputs for email credentials and host to monitor
sender_email = input("Enter the sender email: ")
password = input("Enter the app password: ")
receiver_email = input("Enter the receiver email: ")
host = input("Enter the host to monitor: ")

monitor_host(host, sender_email, password, receiver_email)
