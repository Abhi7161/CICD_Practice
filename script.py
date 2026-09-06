import smtplib
from email.mime.text import MIMEText # Mimetext is a class that represent the text of the email
from email.mime.multipart import MIMEMultipart #Mimemultipart is a class that represent the text of the email message.

import os
def send_email(workflow_name,repo_name, worflow_run_id):
    sender_email=os.getenv('SENDER_EMAIL')
    sender_password=os.getenv('SENDER_PASSWORD')
    receiver_email=os.getenv('RECEIVER_EMAIL')
    subject=f"Workflow {workflow_name} failed for repo {repo_name}"
    body = f"Worflow {workflow_name} failed for repo {repo_name}. Please check the logs for more details\nMore Details:\nRun_ID: {worflow_run_id}"
    msg=MIMEMultipart();
    msg['From']=sender_email
    msg['To']=receiver_email
    msg['Subject']=subject
    msg.attach(MIMEText(body,'plain'))
    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email,sender_password)
        text=msg.as_string()
        server.sendmail(sender_email,receiver_email,text)
        server.quit()
        print('Email sent successfully.')
    except Exception as e:
        print(f"Error : {e}")

send_email(os.getenv('WORKFLOW_NAME'), os.getenv('REPO_NAME'), os.getenv('WORKFLOW_RUN_ID'))