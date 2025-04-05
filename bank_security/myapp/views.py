from django.shortcuts import render

def home(request):
    """Secure banking portal homepage"""
    context = {
        'title': 'Bank of Islington Security Portal',
        'features': [
            'Real-time threat monitoring',
            'Secure transaction validation',
            'Multi-factor authentication',
            'Fraud detection systems'
        ],
        'alert_level': 'secure'  # Options: secure, warning, critical
    }
    return render(request, 'myapp/home.html', context)