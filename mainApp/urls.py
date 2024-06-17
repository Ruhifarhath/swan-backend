from django.urls import path
from . import views
 

urlpatterns = [
    path('',views.home),
    path('announce/', views.announcements_view, name='announcements'),
    path('contact/', views.contact_view, name='contact'), 
    
]
