from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self): # 매직 매서드 (특수목적)
        return f'{self.id}번 글 - {self.title} : {self.content}'
    # str(), print()



# 1. models.py
# 2. python manage.py makemigrations => models.py 바탕으로 설계도(migration 파일) 생성
# 3. python manage.py migrate => DB(db.sqlite3)파일에 설계도를 적용 (테이블 생성)

# DB에 데이터를 생성하는 방법 3가지 CREATE
# 1. article = Article()
#    article.title = "제목" 
#    article.content = '내용'
#    article.save()
# 
# 2. article = Article(title= '두번째', content = '두번째 내용)
#    article.save()
# 
# 3. article = Article.objects.create(title='3번째', content='내용입니다')
# 
# Read
#  1. All - Article.objects.all()
# 
#  2. 1개 - Article.objects.get(id=n) #단수 (인스턴스)
#           Article.bojects.get(title='3번째') #단수 (인스턴스)
#           -unique한 컬럼으로 하는게 좋음.
#           1개만 가져올 수 있음 0개 or 2개 이상은 error발생
# 
#  3. 조건 - Article.objects.filter(title = '3번째')  #복수형 (QuerySet)
#    WHERE
#  4-1. QuerySet + first(), last() # 단수
# 
#  4-2. .order_by(컬럼명)
#       Article.objects.all().order_by('title') # 오름차순
#       Article.objects.all().order_by('-title') # 내림차순
# 
#  4-3. offset, limit (OFFSET, LIMIT) [offset : offset+limit]
#       Article.objects.all()[1:2] => [2]

#  Update
#  1. 데이터 가져오기 - a = Article.objects.get(id=1)
#  2. 수정할 값 할당하기 - a.title = 'first!'
#  3. 저장하기 (DB에 반영하기) - a.save()

#  Delete
#  1. 데이터 가져오기 - a = Article.objects.get(id=1)
#  2. 삭제하기 (DB에 바로 반영) - a.delete()