from mail import Mailer
import os, time
from config import *

appliciant_list = [x.replace("\n", "") for x in open(os.getcwd() + '/list.txt', 'r').readlines()];

mailer = Mailer(MAIL_HOST, MAIL_PORT, MAIL_USER, MAIL_PASS)

mail_subject = "Vernora.com | Interview Request"

mail_message = """
Hello {{NAME}},<br>
We are impressed your application. We would like to make an interview with you.<br>
Please select day and time of interview on <a href="https://vernora.com/interview">https://vernora.com/interview</a>
"""
x=1
for appliciant in appliciant_list:
    if not x == 1: time.sleep(20)
    mail = appliciant.split(',')[0]
    name = appliciant.split(',')[1]
    mail_content = mail_message.replace("{{NAME}}", name)
    mailer.connect_server()
    mailer.send_mail(mail, mail_subject, mail_content)
    print("#" + str(x) + " | Successfully sent mail to %s" % mail)
    mailer.close_server()
    x+=1

print('Interview mails are sent successfully.')