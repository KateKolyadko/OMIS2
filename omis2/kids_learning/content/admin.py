from django.contrib import admin
from content.models import Lesson, Test, Question, Answer

admin.site.register(Lesson)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)