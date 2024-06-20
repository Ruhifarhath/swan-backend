from django.urls import path
from . import views
 

urlpatterns = [
    path('',views.home),
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
     path('patents/', views.patents_view, name='patents'),
     path('sponsors/', views.sponsors_view, name='sponsors'),
     path('gallery/', views.gallery_view, name='gallery'),
      path('prototypes/', views.prototypes_view, name='prototypes'),
      path('ongoing/', views.ongoing_projects, name='ongoing'),
      path('ongoing-1/', views.ongoing_projects_1, name='ongoing-1'),
      path('ongoing-2/', views.ongoing_projects_2, name='ongoing-2'),
      path('ongoing-3/', views.ongoing_projects_3, name='ongoing-3'),
      path('ongoing-4/', views.ongoing_projects_4, name='ongoing-4'),
      path('ongoing-5/', views.ongoing_projects_5, name='ongoing-5'),
      path('ongoing-6/', views.ongoing_projects_6, name='ongoing-6'),
      path('ongoing-7/', views.ongoing_projects_7, name='ongoing-7'),
      path('ongoing-8/', views.ongoing_projects_8, name='ongoing-8'),
      path('ongoing-9/', views.ongoing_projects_9, name='ongoing-9'),
      path('ongoing-10/', views.ongoing_projects_10, name='ongoing-10'),
      path('ongoing-11/', views.ongoing_projects_11, name='ongoing-11'),
      path('ongoing-12/', views.ongoing_projects_12, name='ongoing-12'),

      path('completed/', views.completed_projects, name='completed'),
      path('completed-1/', views.completed_projects_1, name='completed-1'),
      path('completed-2/', views.completed_projects_2, name='completed-2'),
      path('completed-3/', views.completed_projects_3, name='completed-3'),
      path('completed-4/', views.completed_projects_4, name='completed-4'),
      path('completed-5/', views.completed_projects_5, name='completed-5'),
      path('completed-6/', views.completed_projects_6, name='completed'),
      path('completed-7/', views.completed_projects_7, name='completed'),
      path('completed-8/', views.completed_projects_8, name='completed'),
      path('completed-9/', views.completed_projects_9, name='completed'),
      path('completed-10/', views.completed_projects_10, name='completed'),

      path('livedata/', views.live_data_view, name='completed'),



  
    
]
