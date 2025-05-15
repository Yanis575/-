from django.contrib import admin
from.models import Questions, Category
from .views import question


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('questions', 'answer', 'correct', 'category', 'picture')
    list_editable = ('correct', 'category')
    list_per_page = 10
    search_fields = ('questions', 'answer', 'correct')
    list_filter = ('category',)
    ordering = ('questions',)
    list_display_links = ('questions',)

admin.site.register(Category)
