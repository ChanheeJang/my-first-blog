from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# ##--!!(5) 장고 모델에 (우리가 방금 만든!) 몇 가지 변화가 생겼다는 걸 알게 해줘야 
# --> 장고는 데이터베이스에 지금 반영할 수 있도록 마이그레이션 파일(migration file)이라는 것을 준비
# python manage.py makemigrations blog  
# python manage.py migrate blog  # --> 글 모델이 데이터베이스에 저장