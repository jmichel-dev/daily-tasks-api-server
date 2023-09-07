import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from daily_tasks_server.src.config import Config


class SendEmailService:

    @staticmethod
    def send(subject: str, html_message: str, to: str) -> None:
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = Config.EMAIL_SENDER
        message["To"] = to

        mimed_html_message = MIMEText(html_message, "html")
        message.attach(mimed_html_message)

        with smtplib.SMTP(Config.EMAIL_HOST, Config.EMAIL_PORT) as server:
            server.login(Config.EMAIL_LOGIN, Config.EMAIL_PASSWORD)
            server.sendmail(Config.EMAIL_SENDER, to, message.as_string())
