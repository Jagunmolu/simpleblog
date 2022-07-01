from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('', views.PostListCreateView.as_view(), name='all_posts'),
    path('<int:pk>/', views.PostRetrieveUpdateDeleteView.as_view(), name='single_posts'),
]