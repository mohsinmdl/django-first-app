from django.contrib import admin
from .models import Question, Choice
from .models import Entry
from .models import Blog
from .models import Author
# Register your models here.
# admin.site.register(Question)
admin.site.register(Entry)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Choice)

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date','question_text']
#
# admin.site.register(Question,QuestionAdmin)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)