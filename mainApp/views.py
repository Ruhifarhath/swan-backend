from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Announcement


# Create your views here.
def home(request):
    return render(request,'index.html')
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
    return render(request, 'base.html', {'announcements': announcements})