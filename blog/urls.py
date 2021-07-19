
from django.urls import path
from . import views

urlpatterns = [
    path('', views.allBlogs , name='homeBlog'),
    path('<int:blog_id>', views.detail , name='dtlBlog'),
]
