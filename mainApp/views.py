from django.shortcuts import render
from django.http import JsonResponse
from .models import *

from .forms import ContactForm

def home(request):
    announcements = Announcement.objects.all().order_by('-created_at')[:10]  # Fetch latest 10 announcements
    return render(request, 'index.html', {'announcements': announcements})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request'})




def pastMembers_view(request):
    return render(request,'past-members.html')

def mtech_view(request):
    return render(request,'mtechStudents.html')

def mtech_students_view(request):
    students = MTechStudent.objects.all()
    return render(request, 'mtechStudents.html', {'students': students})


def visiting_students_view(request):
    students = VisitingStudent.objects.all()
    return render(request, 'visiting-students.html', {'students': students})


def current_members(request):
    members = Member.objects.all()
    return render(request, 'current-members.html', {'members': members})


def award_winning_papers_view(request):
    papers = AwardWinningPaper.objects.all().order_by('-year')
    return render(request, 'awardPapers.html', {'papers': papers})



def journal_papers_view(request):
    publications = JournalPapers.objects.all().order_by('-year')
    return render(request, 'journalPapers.html', {'publications': publications})

def conference_papers_view(request):
    publications = CoferencePapers.objects.all()
    return render(request, 'conferencePapers.html', {'publications': publications})
    
def book_chapters_view(request):
    publications = BookChapters.objects.all()
    return render(request, 'bookChapters.html', {'publications': publications})
    
def authored_books_view(request):
    publications = AuthoredBooks.objects.all()
    return render(request, 'authoredBooks.html', {'publications': publications})

def edited_books_view(request):
    publications = EditedBooks.objects.all()
    return render(request, 'editedBooks.html', {'publications': publications})

def patents_view(request):
    patents = Patent.objects.all()
    return render(request, 'patents.html', {'patents': patents})

def sponsors_view(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'sponsors.html', {'sponsors': sponsors})

def gallery_view(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})
    
def prototypes_view(request):
    prototypes = Prototype.objects.all()
    return render(request, 'products.html', {'prototypes': prototypes})


