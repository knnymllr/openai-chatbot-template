from django.contrib import admin
from .models import Chat_Message, Chat_Session

# Register your models here.
@admin.register(Chat_Message)
class Chat_Message_Admin(admin.ModelAdmin):
    pass

@admin.register(Chat_Session)
class Chat_Session_Admin(admin.ModelAdmin):
    pass