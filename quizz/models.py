from django.db import models


class UserList(models.Model):
    name = models.CharField(max_length=125)

    class Meta:
        verbose_name_plural = ("Persons")

    def __str__(self):
        return str(self.name)


class Question(models.Model):
    question = models.CharField(max_length=355)
    def options(self):
        if Option.objects.filter(question=self).exists():
            return Option.objects.filter(question=self)
        else:
            return None

    def __str__(self):
        return self.question


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=355)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return str(self.question)


class AttemptHistory(models.Model):
    user = models.ForeignKey(UserList, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = ("Attempt History")

    def __str__(self):
        return str(self.user)


class AnswerRecord(models.Model):
    attempt = models.ForeignKey(AttemptHistory, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_selected = models.ForeignKey(Option, on_delete=models.CASCADE)
    is_correct_option = models.BooleanField(default=False)

    def __str__(self):
        return str(self.attempt.user)
