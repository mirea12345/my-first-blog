from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
   # 속성
   # 외래키 다른 모델을 가리키는 속성, on_delete author가 지워졌을 경우 post 테이블의 데이터
   # cascade는 author가 지워지면 post도 지워지게 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Charfield는 제목이 200자라 길이가 정해져있는 문자열을 담을 때 쓰는 것 
    title = models.CharField(max_length=200)
    # 길이가 정해져있지 않은 문자열 textfield
    text = models.TextField()
    # 날짜 그리고 시간 
    created_date = models.DateTimeField(
            default=timezone.now)
    # 게시글이 퍼블리시된 시간 , 타임존나우: 기본값이 현재시각  
    published_date = models.DateTimeField(
            blank=True, null=True)

# 메서드
    def publish(self):
        # 셀프 자기자신의 오브젝트를 가리키는 약속 
        self.published_date = timezone.now()
        self.save()

# 메서드
    def __str__(self):
        return self.title
    