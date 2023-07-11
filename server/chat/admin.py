from django.contrib import admin
from chat.models import ChatRoom, ChatMessage, ChatUser

admin.site.register(ChatRoom)
admin.site.register(ChatMessage)
admin.site.register(ChatUser)
