from email import message
import smtplib, ssl

port = 465

sender = "projectbookingapi@gmail.com"
password = "vht01042000"

def send_mail(recieve, token):
    message = """
        From: From <projectbookingapi@gmail.com>
        Subject: Token

        {}
    """
    content = message.format(token)
    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, content)
    print("sent email!")