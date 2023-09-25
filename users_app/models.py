from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from .secure.generate_key import Generator
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4


class User (AbstractUser):
    username = None
    groups = None
    first_name = None
    last_name = None


    user_hash_key = models.TextField(_("User Hash Key"),max_length=1000000,null=True,blank=True)
    picture = models.ImageField(upload_to='users-images/',default='default.png')
    is_online = models.BooleanField(default=False)    
    full_name = models.CharField(_('Full Name'),max_length=100)
    email = models.EmailField(_("email address"), unique=True)
    uuid = models.UUIDField(null=True,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name
    
    def login (**kwargs) : 
        email = kwargs['email']
        password = kwargs['password']

        user = User.objects.filter(email=email)
        
        response = {
            'errors':''
        }

        if not user.exists() or user.count() > 1 :
            response['errors'] = 'خطأ في البريد الالكتروني'
            return response
        
        user = user.first()

        if not user.check_password(password) :
            response['errors'] = 'خطأ في كلمة السر'
            return response
        
        response['user'] = user

        return response

@receiver(post_save, sender = User)
def GenreateHashKey (created, instance, **kwargs) :
    if created :
        instance.user_hash_key = Generator()
        instance.uuid = uuid4()
        instance.save()