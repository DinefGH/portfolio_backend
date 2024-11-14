from django.contrib import admin


from django.contrib import admin
from .models import Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('timestamp',)  # Display the timestamp for each visit
    ordering = ('-timestamp',)  # Optional: Order visits by timestamp (newest first)
    list_filter = ('timestamp',)  # Optional: Add a filter by timestamp