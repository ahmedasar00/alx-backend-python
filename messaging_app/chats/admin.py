from django.contrib import admin

# Register your models here.
from .models import chatMessage, ChatRoom, User

admin.site.register(User)
admin.site.register(ChatRoom)
admin.site.register(chatMessage)
# class ChatAdmin(admin.ModelAdmin):
#    list_display = ('id', 'user', 'message', 'timestamp')
#    search_fields = ('user__username', 'message')
# admin.site.register(chatMessage, ChatAdmin)
