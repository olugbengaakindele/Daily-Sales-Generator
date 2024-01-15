from email.message import EmailMessage
import smtplib as sml,ssl, os


# print(os.environ['SALES_DATA_EMAIL_SENDER'])
def sendEmail(file_path,date):
    file_name= f'Sales_report_{date}'
    status = "Not sent"
    sender = os.environ['SALES_DATA_EMAIL_SENDER']
    subject ="This is a test"
    content = f""" 
    Hi Team,

    Please see attached a copy the sales data for {date}. Let me know if you have any questions.

    Thanks

    Olu
    Edatapreneur Inc.
    Canada     
            """

    for rec in os.environ['SALES_DATA_EMAIL_RECEPIENT'].split(","):
        print(rec)
        password = os.environ['GMAILPASS']
        em = EmailMessage()
        em["From"] = sender
        em["To"] = rec
        em["Subject"] = subject
        em.set_content(content)
        context = ssl.create_default_context()

        with open(file_path, 'rb') as f:
            file_data = f.read()
            em.add_attachment(file_data, maintype="application", subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename =file_name)


        with sml.SMTP_SSL('smtp.gmail.com',465, context = context) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, rec, em.as_string())
            status = "email sent"
            print("Email sent")

    return status

# log text to show that it ran
def prepareFile(text):
    file_path = os.path.join(os.getcwd(),"logs.txt")
    if os.path.exists(file_path):
        file = open(file_path,"a")
        file.write(f'{text} \n')
    else:
        file = open(file_path,"w")
        file.write(f'{text}')

    return True
# print(os.environ['SALES_DATA_EMAIL_RECEPIENT'].split(","))