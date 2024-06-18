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
     path('award-winning-papers/', views.award_winning_papers_view, name='award-winning-papers'),
      path('journal-papers/', views.journal_papers_view, name='journalpapers'),
      path('conference-papers/', views.conference_papers_view, name='conference'),
      path('conference-papers/', views.conference_papers_view, name='conference'),
      path('book-chapters/', views.book_chapters_view, name='bookChapters'),
      path('authored-books/', views.authored_books_view, name='authoredBooks'),
      path('edited-books/', views.edited_books_view , name='editedBooks'),
  
    
]
