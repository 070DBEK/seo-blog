from  django.urls import path
from . import views


app_name = 'articles'


urlpatterns = [
    path('list-author/', views.authors_list, name='list-author'),
    path('list-article/', views.articles_list, name='list-article'),
]