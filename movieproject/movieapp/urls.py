
from django.urls import path
from .import views
app_name='movieapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('Movie/<int:Movie_id>/',views.Detail,name="Detail"),
    path('add/', views.add_Movie, name='add_Movie'),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"),
]
