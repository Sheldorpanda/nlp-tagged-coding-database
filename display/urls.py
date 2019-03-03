from django.urls import path

from display import views

urlpatterns = [
    path('', views.ProjectRender, name='project-list'),
    path('', views.search_result, name='search_result')
]
