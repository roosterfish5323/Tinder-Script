import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import ETH_ADDRESS

def send_email(subject, message, to_email):
    # Setup SMTP server
    smtp_server = "smtp.gmail.com"  # Change this to your SMTP server
    smtp_port = 587  # Change this to your SMTP port
    sender_email = "your_email@gmail.com"  # Change this to your email
    sender_password = "your_password"  # Change this to your email password

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(message, 'plain'))

    # Connect to SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send email
    server.sendmail(sender_email, to_email, msg.as_string())

    # Close connection
    server.quit()

def send_auto_messages():
    # Define your matches and messages
    matches = {
        "match1@example.com": "Hey, how are you?",
        "match2@example.com": "Hi there! What are your interests?",
        "match2@example.com": "{}".format(ETH_ADDRESS),
        # Add more matches and messages as needed
    }

    # Define the time to send messages (hour, minute)
    send_time = (10, 0)  # Change this to the desired time

    # Get current time
    now = datetime.datetime.now()

    # Check if it's time to send messages
    if (now.hour, now.minute) == send_time:
        for email, message in matches.items():
            send_email("Automatic Message", message, email)

if __name__ == "__main__":
    send_auto_messages()