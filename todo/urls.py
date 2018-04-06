
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addTodo', views.addTodo, name='addTodo'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall')
]
