from django.db import models
from django.contrib.auth.models import User

class Chat_Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Chat Sessions"
    
    def __str__(self):
        return f"Session {self.session_id}: {self.date}"
    
class Chat_Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    session_id = models.ForeignKey(Chat_Session, on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=256)
    response = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)    
    
    class Meta:
        verbose_name_plural = "Chat Messages"
    
    # See return value in Admin panel
    def __str__(self):
        return f"Message {self.session_id}, {self.message_id}: {self.date}"