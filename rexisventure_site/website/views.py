from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail, EmailMessage

# Create your views here.

def home(request):
    return render(request, "website/home.html")


def capabilities(request):
    return render(request, "website/capabilities.html")


def industries(request):
    return render(request, "website/industries.html")


def government(request):
    return render(request, "website/government.html")


def partners(request):
    return render(request, "website/partners.html")


def about(request):
    return render(request, "website/about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_request = form.save()

            cd = form.cleaned_data

            subject = f"[Rexisventure Contact] {cd.get('subject') or 'New enquiry'}"
            body_lines = [
                "A new contact / RFQ has been submitted via the website.",
                "",
                f"Name:    {cd.get('full_name')}",
                f"Email:   {cd.get('email')}",
                f"Phone:   {cd.get('phone')}",
                f"Company: {cd.get('company')}",
                "",
                "Message:",
                cd.get("message") or "",
                "",
                f"(ContactRequest ID: {contact_request.id})",
            ]
            body = "\n".join(body_lines)

            recipient = getattr(settings, "CONTACT_RECIPIENT", "vendor@rexisventure.com")
            from_email = getattr(settings, "DEFAULT_FROM_EMAIL", None) or cd.get("email")

            try:
                email = EmailMessage(
                    subject=subject,
                    body=body,
                    from_email=from_email,
                    to=[recipient],
                    reply_to=[cd.get("email")] if cd.get("email") else None,
                )
                email.send(fail_silently=False)
                messages.success(
                    request,
                    "Thank you for reaching out. We’ve received your message and will respond as soon as possible.",
                )
            except Exception:
                # Email failed, but we still saved the record in the DB
                messages.warning(
                    request,
                    "Your message was saved, but we could not send an email notification. "
                    "We will still review your request."
                )

            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "website/contact.html", {"form": form})
