from django.urls import path
from . import views

app_name ='lab'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article/', views.ArticleView.as_view(), name='article'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('detail/<int:pk>/', views.ArticleDetailView.as_view(), name='detail_article'),
    path('company/', views.company, name='company')
]