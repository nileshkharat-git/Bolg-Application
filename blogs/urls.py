from django.urls import path

from . import views

urlpatterns = [
    path('publish', views.published_blog, name='publish'),
    path('readblog/<int:blogID>', views.read_blog, name='readBlog'),
    path('showblog',views.show_by_query,name='searchBlog'),
    path('editblog',views.edit_blog,name='editBlog'),
    path('deleteblog',views.delete_blog,name='deleteBlog'),
    path('like/<int:bid>',views.hit_like, name='like'),
]
