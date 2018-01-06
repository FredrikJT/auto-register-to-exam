from read_email import read_email_from_gmail
from send_email import send_email_from_gmail
from check_exams import check_if_exams_exist
from todays_date import todays_date
from PRIVATE import *

#send_parameters = [bot_email, bot_email_pwd, send_to_email, subject, message]
#selenium_parameters = [base_url, page1, page2, pwd, user]

cue = read_email_from_gmail(bot_email, bot_email_pwd)
received_email_subject = cue[0]
received_email_from = cue[1]

if received_email_subject == "Check exams":
    send_parameters[2] = cue[1]
    print("Email with subject \""+received_email_subject+"\" found. Checking for exams.")

    selenium_response = check_if_exams_exist(selenium_parameters)
    print("Response from check: " + selenium_response)

    if isinstance(selenium_response, str):
        if selenium_response == "Inga tentamenstillfällen funna.":
            print("Sending email with response")

            send_parameters[4] = selenium_response
            send_email_from_gmail(send_parameters)

        elif selenium_response == "Exception encountered":
            print("Sending email with Exception encountered")
            send_parameters[4] = "Exception encountered when checking for exams. Please check exams."
            send_email_from_gmail(send_parameters)

        else:
            print("Sending email with alternative response")
            send_parameters[4] = "Please check exams."
            send_email_from_gmail(send_parameters)

    else:
        print("Sending email with alternative response")
        send_parameters[4] = "Please check exams."
        send_email_from_gmail(send_parameters)



######################SCHEDULED CHECK########################

else: #This is the scheduled check
    print("Running scheduled check. Todays date: " + todays_date())
    selenium_response = check_if_exams_exist(selenium_parameters)

    if isinstance(selenium_response, str):

        if selenium_response == "Inga tentamenstillfällen funna.":
            print("Inga tentamenstillfällen funna.")

        elif selenium_response == "Exception encountered":
            print("Sending email with Exception encountered")
            send_parameters[4] = "Exception encountered when checking for exams. Please check exams and script."
            send_email_from_gmail(send_parameters)

        else:
            print("Sending email with alternative response")
            send_parameters[4] = "Please check exams. Something has changed on the site"
            send_email_from_gmail(send_parameters)

    else:
        print("Sending email with alternative response")
        send_parameters[4] = "Please check exams. Something has changed on the site or in the script."
        send_email_from_gmail(send_parameters)

    print("Done with sceduled check.")

