from django.urls import path
from projectapp import views
urlpatterns = [
    path('',views.details,name='details'),
    path('final/',views.finalpage,name='finalpage'),
]