from django.contrib import admin

from polls.models import Question, Choice


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    

class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    # fields = ['pub_date', 'question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ('question_text', 'pub_date')
    search_fields = ('question_text',)
    # search fields uses a LIKE query behind the scenes
    

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'votes')
    list_filter = ('choice_text', 'question', 'votes')
    search_fields = ('choice_text',)
    autocomplete_fields = ('question',)


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)


# 1. Wyświetlić w tabeli wszystkie kolumny z modelu (w obydwu modelach) // done
# 2. W modelu Question dodać pole filtrowania po dacie // done na zajęciach
# 3. Filtrowanie po prawej stronie ekranu (po każdym polu) w obydwu modelach // done
# 4. Pole z wyszukiwaniem w obydwu modelach // done
# 5*. Autouzupełnianie w Question przy tworzeniu Choice