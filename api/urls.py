from django.urls import path
from .views import ListViewPage, UpdateViewPage, UserViewPage, UserDetailViewPage

urlpatterns = [
    path('', ListViewPage.as_view()),
    path('<int:pk>/', UpdateViewPage.as_view()),
    path('users/', UserViewPage.as_view()),
    path('users/<int:pk>/', UserDetailViewPage.as_view()),
]
