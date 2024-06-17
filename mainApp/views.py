from django.shortcuts import render
from django.http import JsonResponse
from .models import *

from .forms import ContactForm

def home(request):
    return render(request, 'index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request'})

def announcements_view(request):
    announcements = Announcement.objects.all().order_by('-created_at')[:10]  # Fetch latest 10 announcements
    return render(request, 'index.html', {'announcements': announcements})


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
# def visiting_view(request):
#     return render(request,'visiting-students.html')
