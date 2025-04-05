def log_access(request, message):
    """Log honeypot access attempts"""
    print(f"[HONEYPOT] {message} from IP: {request.META.get('REMOTE_ADDR')}")

def send_alert(message):
    """Send alerts to admin (customize with email/SMS)"""
    print(f"[ALERT] {message}")
    # Optional: Integrate with Slack/Email
    # requests.post(SLACK_WEBHOOK, json={"text": message})