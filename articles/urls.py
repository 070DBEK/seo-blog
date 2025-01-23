from  django.urls import path
from . import views


app_name = 'articles'


urlpatterns = [
    path('author/create/', views.create_author, name='create_author'),
    path('article/create/', views.create_article, name='create_article'),
    path('articles/comment/create/', views.create_comment, name='create_comment'),
    path(
        'articles/comment/success/<slug:article_slug>/',
        views.comment_success,
        name='comment-success'
    ),
    path(
        'articles/article/<int:year>/<int:month>/<int:day>/<slug:slug>/',
        views.article_detail,
        name='article_detail'
    ),
]