from django.urls import path

from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleCreateView,
    #post
)
urlpatterns = [
    path('new/', ArticleCreateView.as_view(), name = 'article_new'),
    path('', ArticleListView.as_view(), name ='article_list'),
    path('<slug>/edit/', ArticleUpdateView.as_view(), name = 'article_edit'),
    path('<slug>/delete/', ArticleDeleteView.as_view(), name = 'article_delete'),
    path('<slug>/', ArticleDetailView.as_view(), name = 'article_detail'),
]
