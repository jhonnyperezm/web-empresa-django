from django.urls import path
from . import views

urlpatterns = [
#Paths del core
    path('',views.blog, name="blog"),
    path('Category/<int:category_id>/',views.Category, name="category"),
]
