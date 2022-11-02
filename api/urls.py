from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # path('', views.StudentAdd, name="home" ),
    path('add', views.student_add, name="add" ),
    path('update/<int:pk>', views.student_update, name="update" ),
    path('delete/<int:pk>', views.student_delete, name="delete" ),

]
