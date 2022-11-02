from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name="home" ),
    path('add', views.student_add, name="add" ),
    path('update/<int:stud_id>', views.student_update, name="update" ),
    path('delete/<int:stud_id>', views.student_delete, name="delete" ),
]
