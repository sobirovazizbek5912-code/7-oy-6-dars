from django.urls import path
from . import views
from .views import favorites

urlpatterns = [
    path('', views.home, name='home'),
    path('elon/<int:id>/', views.elon_detail, name='detail'),
    path('create/', views.create_elon, name='create'),
    path('update/<int:id>/', views.update_elon, name='update'),
    path('delete/<int:id>/', views.delete_elon, name='delete'),
    path('comment/add/<int:elon_id>/', views.add_comment, name='add_comment'),
    path('comment/delete/<int:id>/', views.delete_comment, name='delete_comment'),
    path('comment/update/<int:id>/', views.update_comment, name='update_comment'),
    path('like/<int:elon_id>/', views.like_elon, name='like_elon'),
    path('favorites/', views.favorites, name='favorites'),
]