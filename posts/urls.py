from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('', views.list_posts, name='all_posts'),
    path('<int:id>/', views.list_post_by_id, name='single_posts'),
]