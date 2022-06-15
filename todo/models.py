from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
# Create your models here.

#  ◦ ID (primary key) - int
#  ◦ Заголовок задачи - char [100]
#  ◦ Описание задачи - text
#  ◦ Срок исполнения - datetime
#  ◦ Выполнено - boolean



class Task(models.Model):
    title = models.CharField(max_length = 100, blank = True, null = True)
    desc = models.TextField(max_length = 5000, blank = True, null = True)
    deadline = models.DateTimeField(null = True, blank = True)
    is_done = models.BooleanField(default=False,null = True, blank = True)

    def __str__(self):
        return "%d | %s" % (self.id, self.title)
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

class User(AbstractUser):
    username=None
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'),max_length=150, unique=True) # changes email to unique and blank to false
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def __str__(self):
        return "%d | %s" % (self.id, self.email)
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
