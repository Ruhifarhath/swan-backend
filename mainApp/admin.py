from django.contrib import admin
from .models import Contact

from .models import Announcement

admin.site.register(Announcement)
admin.site.register(Contact)
