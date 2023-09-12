from django.db import models

from core.abstract.models import AbstractManager, AbstractModel

# Create your models here.

class PostManager(AbstractManager):
    pass

class Post(AbstractModel):
    author = models.ForeignKey(to='core_user.User', on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    
    objects = PostManager()
    
    class Meta:
        db_table = "core_post"
    
    def __str__(self):
        return f'{self.author.name}'

    