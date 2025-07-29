from django.db import models

# Create your models here.
class tbl_user(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=128)  # Store hashed passwords in production

    def __str__(self):
        return self.user_name

