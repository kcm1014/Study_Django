from django.urls import path
from blog.views import post_list, post_detail
urlpatterns = [
    path('list/',post_list),
    path('<int:post_id>/',post_detail),
]