from django.contrib import admin
from .models import Activity, Major, PriceRange, College


class CollegeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("name", "state")}

admin.site.register(PriceRange)
admin.site.register(Activity)
admin.site.register(Major)
admin.site.register(College, CollegeAdmin)