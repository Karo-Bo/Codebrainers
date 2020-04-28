from polls.models import Question, Choice
>>> Question.objects.all()
<QuerySet [<Question: Czy na Brackiej pada?>, <Question: O której powinna być przerwa?>, <Question: Jaki jest twój ulubiony kolor?>]>
>>> qs = Question.objects.all()
>>> str(qs.query)
'SELECT "polls_question"."id", "polls_question"."question_text", "polls_question"."pub_date" FROM "polls_question"'
>>> Question.objects.order_by('question_text')
<QuerySet [<Question: Czy na Brackiej pada?>, <Question: Jaki jest twój ulubiony kolor?>, <Question: O której powinna być przerwa?>]>
>>> str(Question.objects.order_by('question_text').query)
'SELECT "polls_question"."id", "polls_question"."question_text", "polls_question"."pub_date" FROM "polls_question" ORDER BY "polls_question"."question_text" ASC'
>>> str(Question.objects.order_by('-question_text').query)
'SELECT "polls_question"."id", "polls_question"."question_text", "polls_question"."pub_date" FROM "polls_question" ORDER BY "polls_question"."question_text" DESC'
>>> str(Question.objects.order_by('question_text').all().query)
'SELECT "polls_question"."id", "polls_question"."question_text", "polls_question"."pub_date" FROM "polls_question" ORDER BY "polls_question"."question_text" ASC'
>>> Question.objects.filter(question_text__startwith="O").order_by('question_text')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\Bohun\miniconda3\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\Bohun\miniconda3\lib\site-packages\django\db\models\query.py", line 904, in filter
    return self._filter_or_exclude(False, *args, **kwargs)
  File "C:\Users\Bohun\miniconda3\lib\site-packages\django\db\models\query.py", line 923, in _filter_or_exclude
    clone.query.add_q(Q(*args, **kwargs))
  File "C:\Users\Bohun\miniconda3\lib\site-packages\django\db\models\sql\query.py", line 1350, in add_q
    clause, _ = self._add_q(q_object, self.used_aliases)
  File "C:\Users\Bohun\miniconda3\lib\site-packages\django\db\models\sql\query.py", line 1381, in _add_q
    check_filterable=check_filterable,
  File "C:\Users\Bohun\miniconda3\lib\site-packages\django\db\models\sql\query.py", line 1311, in build_filter
    condition = self.build_lookup(lookups, col, value)
  File "C:\Users\Bohun\miniconda3\lib\site-packages\django\db\models\sql\query.py", line 1159, in build_lookup
    lhs = self.try_transform(lhs, lookup_name)
  File "C:\Users\Bohun\miniconda3\lib\site-packages\django\db\models\sql\query.py", line 1200, in try_transform
    "permitted%s" % (name, output_field.__name__, suggestion)
django.core.exceptions.FieldError: Unsupported lookup 'startwith' for CharField or join on the field not permitted, perhaps you meant startswith or istartswith?
>>> Question.objects.filter(question_text__startswith="O").order_by('question_text')
<QuerySet [<Question: O której powinna być przerwa?>]>
>>> str(Question.objects.filter(question_text__startswith="O").order_by('question_text').query)
'SELECT "polls_question"."id", "polls_question"."question_text", "polls_question"."pub_date" FROM "polls_question" WHERE "polls_question"."question_text" LIKE O% ESCAPE \'\\\' ORDER BY "polls_question"."question_text" ASC'
>>> qs = Question.objects.all()
>>> q1 = qs[0]
>>> q1
<Question: Czy na Brackiej pada?>
>>> q1.question_text
'Czy na Brackiej pada?'
>>> q1.id
1
>>> q1.pub_date
datetime.datetime(2020, 4, 25, 12, 34, 29, tzinfo=<UTC>)
>>> q1.question_text = "Czy na Brackiej pada deszcz?"
>>> q1.save()
>>> qs = Question.objects.all()
>>> qs
<QuerySet [<Question: Czy na Brackiej pada deszcz?>, <Question: O której powinna być przerwa?>, <Question: Jaki jest twój ulubiony kolor?>]>
>>> Choice.objects.all()
<QuerySet [<Choice: Tak>, <Choice: Nie>, <Choice: 12.00>, <Choice: 12.30>, <Choice: 13.00>, <Choice: Biały>, <Choice: Czarny>, <Choice: Morski>]>
>>> from django.utils import timezone
>>> q2 = Question(question_text="Jaka jest twoja ulubiona pora roku?", pub_date=timezone.now())
>>> q2
<Question: Jaka jest twoja ulubiona pora roku?>
>>> q2.id
>>> q2.id is None
True
>>> q2.save()
>>> q2.id
4
>>> Question.objects.filter(question_text="Nie istnieje").update(pub_date=xyz)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'xyz' is not defined
>>> Question.objects.filter(question_text="Nie istnieje").delete()
(0, {})
>>> q2
<Question: Jaka jest twoja ulubiona pora roku?>
>>> q2.delete()
(1, {'polls.Question': 1})
>>> q2
<Question: Jaka jest twoja ulubiona pora roku?>
>>> Choice.objects.all()
<QuerySet [<Choice: Tak>, <Choice: Nie>, <Choice: 12.00>, <Choice: 12.30>, <Choice: 13.00>, <Choice: Biały>, <Choice: Czarny>, <Choice: Morski>]>
>>>
>>>
>>> Question.objects.all()
<QuerySet [<Question: Czy na Brackiej pada deszcz?>, <Question: O której powinna być przerwa?>, <Question: Jaki jest twój ulubiony kolor?>]>
>>> q1.choice_set.all()
<QuerySet [<Choice: Tak>, <Choice: Nie>]>
>>> q1.choice_set.order_by('choice_text')
<QuerySet [<Choice: Nie>, <Choice: Tak>]>
>>> q1.choice_set.order_by('-choice_text')
<QuerySet [<Choice: Tak>, <Choice: Nie>]>
>>> q1.choice_set.filter(choice_text__contains='a')
<QuerySet [<Choice: Tak>]>
>>>