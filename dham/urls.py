from django.urls import path
from . views import *

urlpatterns = [
    path('',BooksListAPIView.as_view(),name='books'),
    path('detail/<str:pk>/',BooksDetailAPIView.as_view(),name='detail'),
    # path('create',CreateTodoAPIView.as_view(),name='create'),
    # path('update/<str:pk>/',UpdateTodoAPIView.as_view(),name='update'),
    # path('approved/<str:pk>/',ApprovedTodoAPIView.as_view(),name='approved'),
    # path('delete/<str:pk>/',DeleteTodoAPIView.as_view(),name='delete'),
]