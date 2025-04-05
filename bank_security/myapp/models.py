from django.db import models
from django.contrib.auth.models import User

class UserActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)  # E.g., "Viewed salaries"
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()

    @classmethod
    def log(cls, user, action, request):
        """Log sensitive actions"""
        cls.objects.create(
            user=user,
            action=action,
            ip_address=request.META.get('REMOTE_ADDR')
        )
        # Alert if >5 sensitive actions in 10 mins
        if cls.objects.filter(
            user=user,
            action__contains="sensitive",
            timestamp__gte=timezone.now()-timedelta(minutes=10)
        ).count() > 5:
            send_alert(f"Insider threat: {user.username}")