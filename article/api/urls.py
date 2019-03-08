from django.urls import path, include 
from . import views
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'article', views.ArticleViewSet)

app_name = 'blog_project'

urlpatterns = [
     path('',include(router.urls)),
]


'''
     path('article/',
         views.ArticleListView.as_view(),
         name='article_list'),

     path('article/<pk>/',
         views.ArticleDetailView.as_view(),
         name='article_detail'),

     path('article/create',
         views.ArticleCreateView.as_view(),
         name='article_create'),
         '''