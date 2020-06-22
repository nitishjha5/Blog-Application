from . import views 
from django.urls import path
app_name= 'articles'

urlpatterns = [
    path('', views.articlelist,name= "list"),
    path('create/', views.articlecreate, name= "create"),

    path('<str:p>/', views.articledetails,name="details"),
    
    
] 