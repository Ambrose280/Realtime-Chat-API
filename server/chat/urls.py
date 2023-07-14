from django.urls import path
from chat.views import ChatRoomView, MessagesView, OnlineUserView

urlpatterns = [
	path('chats', ChatRoomView.as_view(), name='chatRoom'),
	path('chats/<str:roomId>/messages', MessagesView.as_view(), name='messageList'),
	path('users/<int:userId>/chats', ChatRoomView.as_view(), name='chatRoomList'),
    path('users/<int:userId>/isactive', OnlineUserView.as_view(), name='chatRoomList'),
]
