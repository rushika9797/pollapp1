from django.contrib import admin

from .models import Choice, Question

# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {"fields": ["question_text"]}),
#         ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
#     ]
#     inlines = [ChoiceInline]


# admin.site.register(Question, QuestionAdmin)
from django.contrib import admin
from .models import Question, Choice

# Inline for Choices (displayed inside Question admin)
class ChoiceInline(admin.TabularInline):  # Use TabularInline for compact table
    model = Choice
    extra = 3  # show 3 empty slots by default

# Customize Question admin
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]  # show Choices inline
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]  # filter sidebar
    search_fields = ["question_text"]  # search box

    # Decorate the was_published_recently for admin
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?"
    )
    def was_published_recently(self, obj):
        return obj.was_published_recently()

# Register Question model
admin.site.register(Question, QuestionAdmin)
