from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

@csrf_exempt
@require_http_methods(["POST"])
def contact_form_handler(request):
    try:
        # Get data from request
        data = json.loads(request.body) if request.content_type == 'application/json' else request.POST
        
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')

        # Validate required fields
        if not all([name, email, subject, message]):
            return JsonResponse({
                'ok': False,
                'message': 'Please fill in all required fields.'
            }, status=400)

        # Create email content
        email_body = render_to_string('email/contact_email.html', {
            'name': name,
            'email': email,
            'message': message,
        })

        # Create and send email
        email = EmailMessage(
            subject=f"Contact Form: {subject}",
            body=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_EMAIL],
            reply_to=[email]
        )
        email.content_subtype = 'html'
        email.send()

        return JsonResponse({
            'ok': True,
            'message': 'Your message has been sent. Thank you!'
        })

    except Exception as e:
        return JsonResponse({
            'ok': False,
            'message': 'There was an error sending your message. Please try again later.'
        }, status=500)
