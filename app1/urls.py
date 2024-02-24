from django.urls import path
from . import views

urlpatterns = [
    path('ecv/', views.emp_create_view, name='create_url'),
    path('elv/', views.emp_list_view, name='list_url'),
    path('euv/<int:pk>/', views.emp_update_view, name='update_url'),
    path('edv/<int:pk>/', views.emp_delete_view, name='delete_url'),
]
