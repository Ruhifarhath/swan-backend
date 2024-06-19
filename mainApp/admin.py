from django.contrib import admin

from .models import *

admin.site.register(MTechStudent)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_new')
    list_editable = ('is_new',) 
admin.site.register(Contact)
admin.site.register(VisitingStudent)
admin.site.register(Member)
admin.site.register(AwardWinningPaper)
admin.site.register(JournalPapers)
admin.site.register(CoferencePapers)
admin.site.register(BookChapters)
admin.site.register(AuthoredBooks)
admin.site.register(EditedBooks)
admin.site.register(Patent)
admin.site.register(Sponsor)
admin.site.register(GalleryImage)
admin.site.register(Prototype)
admin.site.register(Announcement)
admin.site.register(Slide)