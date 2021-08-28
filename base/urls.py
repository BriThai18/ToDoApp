from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='tasks'),
    path('task/<int:id>', views.task, name='task'),
    path('create/', views.taskCreate, name='create'),
    path('update/<int:id>', views.updateTask, name='update'),
    path('delete/<int:id>', views.deleteTask, name='delete'),
    path('registration/', views.registerPage, name='registration'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),

]