from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Grades.as_view()),
    path('<int:id>', views.Grades.as_view()),
    path('employees/', views.Employees.as_view()),
    path('employees/<int:id>', views.Employees.as_view()),
]
