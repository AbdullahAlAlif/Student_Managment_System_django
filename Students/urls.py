from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.index, name='Students_index'),
    path('<int:id>', views.view_student, name='view_student'),
    path('add_student/', views.add, name='add_student'),
    path('edit_student/<int:id>/', views.edit, name='edit_student'),
    path('delete_student/<int:id>/', views.delete, name='delete_student'),
]