import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#send_email_from_gmail(bot_email, bot_email_pwd, send_to_email, subject, message):
def send_email_from_gmail(send_parameters):
    from_email = send_parameters[0]
    from_email_pwd = send_parameters[1]
    send_to_email = send_parameters[2]
    subject = send_parameters[3]
    message = send_parameters[4]
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = send_to_email
    # msg['Subject'] = "Bep bop hello"
    msg['Subject'] = subject
    # body = "Hello bop bep jag r en robot"
    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_email_pwd)
    text = msg.as_string()
    server.sendmail(from_email, send_to_email, text)
    print('Email sent to: ' + send_to_email + '\nWith message: ' + message)
    server.quit()