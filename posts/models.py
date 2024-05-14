from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)

    class Meta: 
        abstract = True

class Post(BaseModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="제목", max_length=20)
    author = models.CharField(verbose_name="작성자", max_length=10)
    content = models.TextField(verbose_name="내용")
    passcode = models.CharField(verbose_name="게시글 비밀번호", max_length=15)