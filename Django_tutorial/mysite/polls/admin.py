from django.contrib import admin

from polls.models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('question_text', 'pub_date')
    list_filter = ('question_text', 'pub_date')
    search_fields = ('question_text',)
    

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'votes')
    list_filter = ('choice_text', 'question', 'votes')
    search_fields = ('choice_text',)
    autocomplete_fields = ('question',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)


# 1. Wyświetlić w tabeli wszystkie kolumny z modelu (w obydwu modelach) // done
# 2. W modelu Question dodać pole filtrowania po dacie // done na zajęciach
# 3. Filtrowanie po prawej stronie ekranu (po każdym polu) w obydwu modelach // done
# 4. Pole z wyszukiwaniem w obydwu modelach // done
# 5*. Autouzupełnianie w Question przy tworzeniu Choice