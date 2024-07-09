from django.urls import path
from .views import UserController

urlpatterns = [
    path('user/', UserController.as_view(), name='create_user'),
    path('user/<int:id>', UserController.as_view(), name='get_user'),
    path('user/<int:id>', UserController.as_view(), name='delete_user'),
    path('user/<int:id>', UserController.as_view(), name='update_user'),
]