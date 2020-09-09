from django.db import models

# Create your models here.

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=800)
    date = models.DateTimeField("Date Published",auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("Title", max_length=60)
    img = models.ImageField(null=True)
    short_desc = models.TextField("Short Description", max_length=90)
    desc = models.TextField("Description")
    date_published = models.DateTimeField("Date Published", auto_now_add=True)

    def __str__(self):
        return self.title

