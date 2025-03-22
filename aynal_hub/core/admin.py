from django.contrib import admin
from .models import Tutorial

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author_name', 'is_published', 'is_featured', 'published_date')
    
    # Fields that can be edited directly in the list view
    list_editable = ('is_published', 'is_featured')
    
    # Fields to filter the list view by
    list_filter = ('is_published', 'is_featured', 'published_date', 'category')
    
    # Fields to search in the list view
    search_fields = ('title', 'author_name', 'short_description', 'content')
    
    # Fields to prepopulate based on other fields
    prepopulated_fields = {'slug': ('title',)}
    
    # Group fields into sections for the add/edit form
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'short_description', 'content'),
        }),
        ('Media', {
            'fields': ('cover_image', 'thumbnail', 'author_image'),
        }),
        ('SEO and Visibility', {
            'fields': ('meta_description', 'is_published', 'is_featured', 'published_date'),
        }),
        ('Author Information', {
            'fields': ('author_name', 'author_bio'),
        }),
        ('Categories and Tags', {
            'fields': ('category', 'tags'),
        }),
    )
    
    # Add a date hierarchy for easy navigation by date
    date_hierarchy = 'published_date'
    
    # Add a custom action to mark tutorials as published
    actions = ['mark_as_published']
    
    def mark_as_published(self, request, queryset):
        queryset.update(is_published=True)
    mark_as_published.short_description = "Mark selected tutorials as published"