import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Template
from dataclasses import dataclass, field
import os



class TemplateDoesNotExist(Exception):
    pass


@dataclass
class Pygmail:
    smtp_username: str
    app_password: str  # Gmail app password -> https://myaccount.google.com/apppasswords
    smtp_server: str = field(default="smtp.gmail.com")
    smtp_port: int = field(default=587)


    def send_email(self, sender_email: str, receiver_email: str, subject: str, template_path: str, context: dict) -> str:

        """ Read and render the HTML template """
        if not os.path.exists(template_path):
            raise TemplateDoesNotExist(f"The template file '{template_path}' does not exist.")
        
        try:
            with open(template_path, "r") as file:
                template = Template(file.read())
        except FileNotFoundError:
            raise TemplateDoesNotExist(f"The template file '{template_path}' was not found.")
        except Exception as e:
            raise Exception(f"Error reading template file: {e}")

        html_content = template.render(context)


        """ Create the email message """   
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        """ Attach the HTML content """
        msg.attach(MIMEText(html_content, "html"))

        """ Send the email """

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.smtp_username, self.app_password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                return "email sent successfully."
        except Exception as e:
            print(f"Error sending email: {e}")
            return 'email not sent!'


