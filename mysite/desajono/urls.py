from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>/<int:month>/<slug:slug>/', views.see_article, name='article-detail'),
    path('technopark/', views.open_technopark, name='technopark'),
]
