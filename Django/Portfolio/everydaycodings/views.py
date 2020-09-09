from django.shortcuts import render, HttpResponse
from .models import Contact, Project
from django.contrib import messages

# Create your views here.
def index(request):
    project = Project.objects.order_by("-id")[:3]

    if request.method == "POST":
        name = request.POST["name"]
        subject = request.POST["subject"]
        email = request.POST["email"]
        message = request.POST["message"]
        contact = Contact(name=name, subject=subject, email=email, message=message)

        if len(name) < 3 or len(subject) < 5 or len(email) < 5 or len(message) < 10:
            messages.error(request, "Please Recheck the Contact form we think that your wrote something wrong or some data is Incorrect!!")
        else:
            contact.save()
            messages.success(request, "Your message is successfully sent to the Admin :) ")

    context ={"projects": project}

    return render(request, "everydaycodings/index.html", context)


def single_post(request, id):
    
    post = Project.objects.filter(id=id).first()

    context = {"post": post}

    return render(request, "everydaycodings/post.html", context)