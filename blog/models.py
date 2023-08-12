from django.db import models

# Create your models here.
# 포스트 제목 은 title을 한국어로 포스트 제목으로 보여준다.
class Post(models.Model):
    title = models.CharField('포스트 제목', max_length=100)
    content = models.TextField('포스트 내용')
    thumbnail = models.ImageField("썸네일 이미지",upload_to="post", blank=True)  # makemigrations 에러 발생시 pip install pillow<10 을 이용하여 pillow 설치 필요
                                                                              # upload_to 는 업로드 될 폴더를 지정 /media/post에 저장됨
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField('댓글 내용')

    def __str__(self):
        return f'{self.post.title}의 댓글 (ID : {self.id})'