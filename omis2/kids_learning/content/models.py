from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    content = models.TextField()
    difficulty_level = models.CharField(max_length=20)
    multimedia = models.FileField(upload_to='')



class Test(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions_list', on_delete=models.CASCADE)  # Изменено related_name
    question_text = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers_list', on_delete=models.CASCADE)  # Изменено related_name
    answer_text = models.CharField(max_length=100)

    def __str__(self):
        return self.answer_text
    

