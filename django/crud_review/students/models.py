from django.db import models

# Create your models here.
class Students(models.Model):
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self): # 매직 매서드 (특수목적)
        return f'{self.id}번 학생 -이름 : {self.name} , 나이 : {self.age}'

    # 1. python manage.py makemigrations

    # 2. python manage.py migrate 실행