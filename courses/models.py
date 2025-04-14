from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# course model rep. online course
class Course(models.Model):
    # title of course
    title = models.CharField(max_length = 150)
    # short description
    description = models.TextField(blank = True)
    # category (programming, linear alg., etc)
    category = models.CharField(max_length = 100, blank = True)
    # date when course published
    publication_date = models.DateField(null = True, blank = True)
    
    def __str__(self):
        # ret. title as str. rep.
        return self.title
