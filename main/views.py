from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "index.html")



def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        full_message = f"Message from {name} ({email}):\n\n{message}"

        send_mail(
            subject="New Portfolio Contact",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        messages.success(request, "✅ Your message has been sent successfully!")
        return redirect("home")  # change "home" to your index url name

    return render(request, "index.html")