import smtplib
import json
from email.mime.text import MIMEText

# Load Zoho SMTP config
with open("config.json") as f:
    config = json.load(f)

def send_via_zoho(to_email, subject, html_content):
    try:
        msg = MIMEText(html_content, "html")
        msg["Subject"] = subject
        msg["From"] = config["email"]
        msg["To"] = to_email

        server = smtplib.SMTP(config["smtp_server"], config["smtp_port"])
        server.starttls()
        server.login(config["email"], config["password"])
        server.sendmail(config["email"], to_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print("Error sending mail:", e)
        return False
