from django.contrib import admin
from .models import Activity, Major, PriceRange, College
# Register your models here.

class CollegeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("name", "location")}

admin.site.register(PriceRange)
admin.site.register(Activity)
admin.site.register(Major)
admin.site.register(College, CollegeAdmin)