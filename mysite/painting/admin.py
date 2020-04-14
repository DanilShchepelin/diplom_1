from django.contrib import admin
from .models import Reviews, Pictures, Lessons, Like

"""
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'reviews')
    search_fields = ('name', 'reviews')
"""

admin.site.register(Reviews)
admin.site.register(Pictures)
admin.site.register(Lessons)
admin.site.register(Like)
