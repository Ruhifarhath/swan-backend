from django.urls import path
from . import views
 

urlpatterns = [
    path('',views.home),
    path('announce/', views.announcements_view, name='announcements'),
    path('contact/', views.contact_view, name='contact'), 
    path('currentmembers/',views.currentMembers_view, name="currentmembers"),
    path("pastmembers/", views.pastMembers_view,name='pastmembers'),
    path('mtech/', views.mtech_view,name='mtech'),
    # path('visitingStudents', views.visiting_view,name='visiting'),
    
]
