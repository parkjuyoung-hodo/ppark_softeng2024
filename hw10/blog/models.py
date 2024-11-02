from django.db import models

# Create your models here.
# 모델을 많이 만질것이다

class Post(models.Model):
    title =models.CharField(max_length=30)  # 30자 만 쓰겠다
    content= models.TextField()

    created_at =models.DateTimeField()  # auto_now_add-> 이거 쓰면 시간 저장 안됨
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.pk:}] {self.title}" # rmfqjsgh wnf cnffur

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'