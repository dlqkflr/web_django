from django.db import models

# Create your models here.
class Movies(models.Model):
    #id = models.AutoField(primary_key=True)
    title = models.CharField(max_length= 30)
    title_en = models.CharField(max_length= 30)
    audience = models.IntegerField()
    open_date = models.DateTimeField()
    genre = models.CharField(max_length= 10)
    watch_grade = models.CharField(max_length= 10)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

    # def __str__(self): # 매직 매서드 (특수목적)
    #     return f'{self.id}번 학생 -이름 : {self.name} , 나이 : {self.age}'

    # 1. python manage.py makemigrations

    # 2. python manage.py migrate 실행