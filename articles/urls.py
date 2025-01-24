from  django.urls import path
from . import views


app_name = 'articles'


urlpatterns = [
    path('author/create/', views.create_author, name='create_author'),
    path('article/create/', views.create_article, name='create_article'),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.article_detail,
         name='detail'
         ),
    path(
        'comment-success/<slug:slug>/',
         views.comment_success,
         name='comment-success'
    ),
]