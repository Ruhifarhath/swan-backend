from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd
from .models import *

# Export functions
def export_to_excel(model):
    data = list(model.objects.values())
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={model._meta.model_name}.xlsx'
    df.to_excel(response, index=False)
    return response

def export_to_pdf(model):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={model._meta.model_name}.pdf'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter
    y = height - 40

    data = model.objects.all()
    for entry in data:
        fields = [f"{field.name}: {getattr(entry, field.name)}" for field in entry._meta.fields]
        for field in fields:
            p.drawString(30, y, field)
            y -= 20
            if y < 40:
                p.showPage()
                y = height - 40

    p.save()
    return response

# Custom admin class with export actions
class ExportAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('export/excel/', self.admin_site.admin_view(self.export_excel), name='export_excel'),
            path('export/pdf/', self.admin_site.admin_view(self.export_pdf), name='export_pdf'),
        ]
        return custom_urls + urls

    def export_excel(self, request):
        model = self.model
        return export_to_excel(model)

    def export_pdf(self, request):
        model = self.model
        return export_to_pdf(model)

    actions = ["export_as_excel", "export_as_pdf"]

    def export_as_excel(self, request, queryset):
        model = self.model
        return export_to_excel(model)

    export_as_excel.short_description = "Export Selected to Excel"

    def export_as_pdf(self, request, queryset):
        model = self.model
        return export_to_pdf(model)

    export_as_pdf.short_description = "Export Selected to PDF"

# Registering models with ExportAdmin
admin.site.register(AwardWinningPaper, ExportAdmin)
admin.site.register(JournalPapers, ExportAdmin)
admin.site.register(CoferencePapers, ExportAdmin)
admin.site.register(BookChapters, ExportAdmin)
admin.site.register(AuthoredBooks, ExportAdmin)
admin.site.register(EditedBooks, ExportAdmin)
admin.site.register(Patent, ExportAdmin)

# Other admin registrations
admin.site.register(MTechStudent)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_new')
    list_editable = ('is_new',) 
admin.site.register(Contact)
admin.site.register(VisitingStudent)
admin.site.register(Member)
admin.site.register(Sponsor)
admin.site.register(GalleryImage)
admin.site.register(Prototype)
admin.site.register(Announcement)
admin.site.register(Slide)
