# made by umakoshi masato
from django.db import models
from django.contrib.auth.models import User


class ImageChoice(models.Model):
    """Model for image choice of user.

    Author:
        Masato Umakoshi
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    url_path = models.CharField(max_length=100)

    def __str__(self):
        return self.url_path

    def __iter__(self):
        """This special method was added to dealing with bug on production environment.
        """
        return self.url_path.__iter__()
