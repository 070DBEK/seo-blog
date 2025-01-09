from  django.urls import path
from . import views


app_name = 'articles'


urlpatterns = [
    path('add-author/', views.create_author, name='add-author'),
    path('add-article/', views.create_article, name='add-article'),
]