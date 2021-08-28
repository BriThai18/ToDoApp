from django.db import models
#User model takes care of user information and authentication 
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta():
        #Order by status of complete
        ordering = ['complete']

