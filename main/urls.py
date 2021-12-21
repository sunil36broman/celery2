from django.urls import path
from . views import *

urlpatterns = [
    path('',BooksListAPIView1.as_view(),name='books1'),
    path('category/',BooksListAPIView11.as_view(),name='books11'),
    path('detail/<str:pk>/',BooksDetailAPIView1.as_view(),name='detail1'),
    path('schedulemail/', schedule_mail, name='schedulemail'),
    # path('create',CreateTodoAPIView.as_view(),name='create'),
    # path('update/<str:pk>/',UpdateTodoAPIView.as_view(),name='update'),
    # path('approved/<str:pk>/',ApprovedTodoAPIView.as_view(),name='approved'),
    # path('delete/<str:pk>/',DeleteTodoAPIView.as_view(),name='delete'),
]