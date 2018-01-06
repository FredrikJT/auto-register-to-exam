import smtplib
import time
import imaplib
import email
import io
import sys

SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

def read_email_from_gmail(FROM_EMAIL, FROM_PWD):
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'UNSEEN') #Read emails with tag "Unseen"
        mail_ids = data[0]

        id_list = mail_ids.split()

        if not id_list:
            print('No new emails.')
            return "No new emails."

        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id-1, -1):
            typ, data = mail.fetch(str(i), '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    email_content = data[0][1]
                    msg = email.message_from_bytes(email_content)
                    email_subject = msg['subject']
                    email_from = msg['from']
                    email_message = msg.get_payload(1).get_payload()
                    print("\nEmail found!")
                    print('Email from : ' + email_from)
                    print('Email subject : ' + email_subject)
                    print('Email message: ' + email_message)

                    if email_subject == "Check exams":
                        return [email_subject, email_from]

    except Exception as e:
        print(str(e))
        return e