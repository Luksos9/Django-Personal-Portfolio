from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/') # najlatiwje utworzyc media folder/portfolio/images/
    image2 = models.ImageField(upload_to='portfolio/images/', blank=True) # najlatiwje utworzyc media folder/portfolio/images/
    url = models.URLField(blank=True) # blank - true, czy


    def __str__(self):
        return self.title

