from django.urls import path
from . import views

urlpatterns = [
       path('', views.add_show,name='AddAndShow'),
       path('delete/<int:id>/', views.delete_data, name='DeleteData'),
       path('<int:id>/', views.update_data, name='UpdateData'),
]
