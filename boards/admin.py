

from django.contrib import admin
from .models import ForumSectionModel, forummodel
from django.utils.safestring import mark_safe
from .models import CommentModel
# admin.site.register(forummodel)
# admin.site.register(CommentModel)
# admin.site.register(ForumSectionModel)
from django.utils.translation import gettext_lazy as _

site_header = "My Custom Admin Header"  # Header text
site_title = "My Admin Panel"           # Title in the browser tab
index_title = "Welcome to My Admin"    # Title on the admin homepage

@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('massg', 'section', 'created_by', 'created_dt', 'updated_by', 'updated_dt')
    search_fields = ('massg', 'section__name', 'created_by__username')
    list_filter = ('created_dt', 'section')
    ordering = ('-created_dt',)
      
@admin.register(forummodel)
class ForumModelAdmin(admin.ModelAdmin):
    list_display = ('ForumTitile', 'ForumDescription', 'ForumImage')
    search_fields = ('ForumTitile',)
    list_filter = ('ForumTitile',)
    list_editable=('ForumDescription',)
    
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.ForumImage.url}" style="width: 40px; height: 40px; object-fit: cover;"/>')
        return 'No Image'
    image_preview.short_description = 'Image Preview'  # Title for the column     

@admin.register(ForumSectionModel)
class ForumSectionModelAdmin(admin.ModelAdmin):
    list_display = ('SectionSubject', 'board', 'created_by', 'views', 'created_dt', 'updated_by', 'updated_dt')
    search_fields = ('SectionSubject', 'board__ForumTitile', 'created_by__username')
    list_filter = ('board', 'created_dt', 'updated_dt')
    autocomplete_fields = ('board', 'created_by', 'updated_by')
    exclude = ('created_dt',)  # Exclude non-editable fields from the admin form

    ordering = ('-created_dt',)

