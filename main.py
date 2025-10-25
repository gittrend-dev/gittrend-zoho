from fastapi import FastAPI
from fetch_trending import get_trending
from generate_html import generate_html
from send_mail_zoho import send_via_zoho

app = FastAPI()

@app.get("/trending")
def trending_test():
    """Return top 10 trending repos as JSON"""
    return get_trending(limit=10)

@app.get("/send-mail")
def send_mail_test():
    """Send a test email via Zoho"""
    repos = get_trending(limit=5)
    html = generate_html(repos)
    success = send_via_zoho(
        to_email="user@example.com",
        subject="GitTrend Test Email",
        html_content=html
    )
    return {"sent": success}
