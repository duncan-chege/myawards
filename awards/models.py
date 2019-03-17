from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length =50)
    description = models.CharField(max_length =100)
    image_path = models.ImageField(upload_to='project_images/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    website_link= models.CharField(max_length =100)

    def __str__(self):
        return self.title

