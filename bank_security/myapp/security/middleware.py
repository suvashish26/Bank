
import re
from django.http import HttpResponseForbidden

class WAFMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # Required for Django middleware
        self.blocked_patterns = [
            r'<script>',       # XSS
            r'SELECT.*FROM',   # SQLi
            r'\.\./',          # Path traversal
        ]

    def __call__(self, request):  # Required method
        # Process the request
        response = self.process_request(request)
        if response:  # If blocked by WAF
            return response
            
        # Continue with normal processing
        return self.get_response(request)

    def process_request(self, request):
        for param in request.GET | request.POST:
            param_str = str(param)
            for pattern in self.blocked_patterns:
                if re.search(pattern, param_str, re.IGNORECASE):
                    self.log_attack(request, pattern)
                    return HttpResponseForbidden("Blocked by WAF")
        return None

    def log_attack(self, request, pattern):
        print(f"[WAF] Blocked {pattern} from {request.META.get('REMOTE_ADDR')}")