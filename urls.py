from django.contrib import admin
from django.urls import path, re_path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.articles_list, name="articles_list"),
    re_path(r"^article/(?P<article_id>\w+)", views.view_article, name="view_article"),
] 
