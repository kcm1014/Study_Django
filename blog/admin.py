from django.contrib import admin
from blog.models import Post, Comment
# Register your models here.
@admin.register(Post)
class adminPost(admin.ModelAdmin):
    list_display = ['title','thumbnail']  # Post 데이터를 선택했을 때 보열줄 컬럼 목록

@admin.register(Comment)
class adminComment(admin.ModelAdmin):
    pass