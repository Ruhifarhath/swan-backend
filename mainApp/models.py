# models.py
from django.db import models

class Slide(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='slides/')
    link = models.URLField(blank=True, null=True)


class Prototype(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='prototypes/')
    link = models.URLField()

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    description = models.CharField(max_length=255, blank=True)

class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='sponsors/')
    link = models.URLField(blank=True, null=True)

class Patent(models.Model):
    application_number = models.CharField(max_length=255)
    publication_date = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)

class EditedBooks(models.Model):
    award = models.CharField(max_length=255)
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)
    link = models.URLField(blank=True, null=True)

class AuthoredBooks(models.Model):
    award = models.CharField(max_length=255)
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)
    link = models.URLField(blank=True, null=True)

class BookChapters(models.Model):
    book_title=models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    chapter_title = models.CharField(max_length=200, blank=True, null=True)
    pages = models.CharField(max_length=20, blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    doi = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField(max_length=500, blank=True, null=True)

class CoferencePapers(models.Model):
    award = models.CharField(max_length=255)
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)
    link = models.URLField(blank=True, null=True)


class JournalPapers(models.Model):
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)
    journal = models.CharField(max_length=255)
    year = models.IntegerField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class AwardWinningPaper(models.Model):
    award = models.CharField(max_length=255)
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)
    journal = models.CharField(max_length=255)
    year = models.IntegerField()
    volume = models.CharField(max_length=50, blank=True, null=True)
    issue = models.CharField(max_length=50, blank=True, null=True)
    pages = models.CharField(max_length=50, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(default='')
    is_new = models.BooleanField(default=False)  

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
    is_current = models.BooleanField(default=True)

    def __str__(self):
        return self.name