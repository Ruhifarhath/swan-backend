from django.urls import path
from . import views
 

urlpatterns = [
    path('',views.home),
    path('announce/', views.announcements_view, name='announcements'),
    path('contact/', views.contact_view, name='contact'), 
    path("pastmembers/", views.pastMembers_view,name='pastmembers'),
    path('mtech-students/', views.mtech_students_view, name='mtech-students'),
     path('visiting-students/', views.visiting_students_view, name='visiting-students'),
    path('current-members/', views.current_members, name='current_members'),
  
    
]
