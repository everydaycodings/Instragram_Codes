from django.contrib import admin
from .models import Contact, Project
from import_export.admin import ImportExportModelAdmin

# Register your models here.
#admin.site.register(Contact)
#admin.site.register(Project)


@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
   list_display = ("name", "email", "date")

@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    list_display = ("title", "date_published")
    class Media:
        css = {
            "all": ("scss/blog.css", )
        }
        js = ("everydaycodings/js/blog.js",)