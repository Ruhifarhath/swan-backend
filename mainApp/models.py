# models.py
from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(default='')

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