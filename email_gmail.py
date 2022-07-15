from email.message import EmailMessage
from smtplib import SMTP_SSL
from cred_store_local import EMAIL_PASS, EMAIL_USERNAME, EMAIL_SENDER, EMAIL_RECEIVER


def send_email(subject: str, content: str) -> None:

    smtp_server = 'smtp.gmail.com'
    username = EMAIL_USERNAME
    password = EMAIL_PASS

    sender = EMAIL_SENDER
    destination = EMAIL_RECEIVER

    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(content)

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = destination

    try:
        smtpserver = SMTP_SSL(smtp_server)
        smtpserver.login(username, password)
        try:
            smtpserver.send_message(msg)
        finally:
            smtpserver.quit()

    except Exception as E:
        print(f'Mail failed: {str(E)}')


if __name__ == "__main__":
    subject = 'Test Email Subject'
    content = 'Test Email Body'
    send_email(subject, content)
