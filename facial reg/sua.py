import smtplib
from email.mime.text import MIMEText

def send_email_alert():
    sender_email = "nbd@gmail.com"
    receiver_email = "abc@example.com"
    password = "abc@908"  # Or use app password if 2FA enabled

    subject = "Alert: Unknown Person Detected"
    body = "An unknown person was detected at your entry point."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)  # Login with your password or app password
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email and password.")
    except Exception as e:
        print(f"Error: {e}")

# Call the function
send_email_alert()
