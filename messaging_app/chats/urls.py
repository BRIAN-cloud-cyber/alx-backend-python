from django.urls import path
from . import views

urlpattersn=[
    path('',views.index,name='chat_index'),
          
    path('<int:room_id>/',views.room,name='chat_room'),
]