from django.contrib import admin
from .models import Question, UserList, AnswerRecord, Option, AttemptHistory


@admin.register(UserList)
class UserListAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('question', 'option')


@admin.register(AnswerRecord)
class AnswerRecordAdmin(admin.ModelAdmin):
    pass


@admin.register(AttemptHistory)
class AttemptHistoryAdmin(admin.ModelAdmin):
    pass
