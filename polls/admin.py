from django.contrib import admin
from .models import Choice,Question
# Register your models here.
admin.site.site_header="The Poll Site"
admin.site.site_title="Voting Admin Area"
admin.site.index_title="Welcome to our Voting Admin Area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"],"classes":
                              ["collapse"]}),
   # list_display = ["question_text", "pub_date"]
    ]
    inlines=[ChoiceInline]


admin.site.register(Question, QuestionAdmin)
