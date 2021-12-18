from django.urls import path
from .views import *

urlpatterns = [
    path('', ListViewPage.as_view(), name='article_list'),
    path('<int:pk>/', DetailViewPage.as_view(), name='article_detail'),
    path('<int:pk>/edit/', UpdateViewPage.as_view(), name='article_edit'),
    path('<int:pk>/delete/', DeleteViewPage.as_view(), name='article_delete'),
    path('new/', CreateViewPage.as_view(), name='article_new'),
]
