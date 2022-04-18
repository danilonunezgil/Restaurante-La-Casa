from django.urls import path
from newsletter import views

app_name = 'newsletter'

urlpatterns = [
    path('', views.NewsListView, name='news-list'),
    path('<str:parent_or_child>/<int:pk>', views.NewsListView, name='news_cat'),
    path('<id>/', views.NewsDetailView.as_view(), name='news-detail'),
]