from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

class Mailer:
    def __init__(self, smtp_host, smtp_port, smtp_user, smtp_password):
        self.host = smtp_host
        self.port = smtp_port
        self.user = smtp_user
        self.passw = smtp_password
        
    
    def connect_server(self):
        try:
            self.conn = SMTP(self.host, self.port)
            print("Connection successfully. Logging in...")
            self.conn.set_debuglevel(False)
            self.conn.login(self.user, self.passw)
            self.conn.ehlo("Vernora.com")
            print("SMTP connection successful.")
        except Exception as e:
            print(e)
            print("SMTP connection failed. Closing application.")
            exit()

    def send_mail(self, mail, subject, content):
        message = MIMEText(content, 'html')
        message['Subject'] = subject
        message['From'] = self.user
        try:
            self.conn.sendmail(self.user, mail, message.as_string())
        except Exception as e:
            print(e)
            print("While sending mail an error occurred. Closing application.")
            exit()

    def close_server(self):
        self.conn.quit()
        print("Mail server closed successfully. Application closing now..")