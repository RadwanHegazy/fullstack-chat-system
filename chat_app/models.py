from django.db import models
from users_app.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

class Chat (models.Model) :
    users = models.ManyToManyField(User)
    uuid = models.UUIDField(null=True,blank=True)
    last_msg = models.CharField(max_length=100,null=True,blank=True)

    def get_friend (self, user) : 
        for u in self.users.all() :
            if u != user :
                return u

    def __str__(self) : 
        return f"{self.users.all()[0]}, {self.users.all()[1]}"
    
class Message (models.Model): 
    date = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE)
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=10000000,null=True,blank=True)
    image = models.ImageField(upload_to='chat-images',null=True,blank=True)
    audio = models.ImageField(upload_to='chat-audio',null=True,blank=True)

    def __str__(self) : 
        return str(self.chat)
    


@receiver(post_save, sender = Chat)
def CreateChatUUid(created, instance, **kwargs) :
    if created :
        instance.uuid = uuid.uuid4()
        instance.save()


@receiver(post_save, sender = Message)
def UpdateLastMessage(created, instance, **kwargs) :
    if created :

        if instance.text :
            msg = f'{instance.sender} : {instance.text}'
        else : 
            msg = f'{instance.sender} : Media'
        
        instance.chat.last_msg = msg
        instance.chat.save()
