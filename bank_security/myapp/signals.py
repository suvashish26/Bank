# # myapp/signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.utils import timezone
# from datetime import timedelta
# from .models import UserActivityLog  # Make sure to import your model

# def alert_security_team(message):  # Add this helper function
#     """Replace with actual alert logic (email/SMS/Slack)"""
#     print(f"SECURITY ALERT: {message}")  # Temporary implementation

# @receiver(post_save, sender=UserActivityLog)
# def detect_anomalies(sender, instance, **kwargs):
#     if instance.action == "Sensitive Data Access":
#         recent_actions = UserActivityLog.objects.filter(
#             user=instance.user,
#             timestamp__gte=timezone.now() - timedelta(minutes=5)
#         )  # Fixed: Added closing parenthesis
#         if recent_actions.count() > 10:  # Threshold
#             alert_security_team(f"Insider threat detected: {instance.user}")