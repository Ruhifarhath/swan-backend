# models.py
from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(default='')

class MTechStudent(models.Model):
    name = models.CharField(max_length=200)
    thesis_title = models.CharField(max_length=500)
    thesis_year = models.CharField(max_length=50)
    co_supervisor = models.CharField(max_length=200, blank=True, null=True)

class VisitingStudent(models.Model):
    name = models.CharField(max_length=200)
    thesis_title = models.CharField(max_length=500)
    intern_duration = models.CharField(max_length=100)
    additional_info = models.CharField(max_length=500, blank=True, null=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    ROLE_CHOICES = [
        ('Guide', 'Guide'),
        ('Visiting Professor', 'Visiting Professor'),
        ('Post-Doc Student', 'Post-Doc Student'),
        ('Ph.D. Student', 'Ph.D. Student'),
        ('M.S. Student', 'M.S. Student'),
    ]
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50, choices=ROLE_CHOICES)
    photo = models.ImageField(upload_to='members/')
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name