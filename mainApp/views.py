from django.shortcuts import render
from django.http import JsonResponse
from .models import Announcement

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

def currentMembers_view(request):
    return render(request,'current-members.html')

def pastMembers_view(request):
    return render(request,'past-members.html')

def mtech_view(request):
    return render(request,'mtechStudents.html')

# def visiting_view(request):
#     return render(request,'visiting-students.html')
