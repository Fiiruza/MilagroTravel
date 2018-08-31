from django.contrib import admin
from .models import *

admin.site.register(Tour)


class NewsPostAdmin(admin.ModelAdmin):
    ordering = ('-published_date',)


admin.site.register(NewsPost, NewsPostAdmin)


class RequestAdmin(admin.ModelAdmin):
    ordering = ('-created_date',)


admin.site.register(Request, RequestAdmin)