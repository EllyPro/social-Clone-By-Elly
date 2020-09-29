from django.urls import path
from . import views

app_name = 'groups'

urlpatterns =[
    path('',views.ListGroup.as_view(),name='all'),
    path('create/',views.CreateGroup.as_view(),name='create'),
    path('posts/in/<str:slug>',views.SingleGroup.as_view(),name='single'),
    path('join/<str:slug>/group',views.JoinGroup.as_view(),name='join'),
    path('leave/<str:slug>/group',views.LeaveGroup.as_view(),name='leave'),
]
