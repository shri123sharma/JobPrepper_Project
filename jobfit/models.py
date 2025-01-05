from django.db import models
# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    published_date=models.DateField()
    isbn=models.CharField(max_length=255,unique=True)
    available=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}-{self.author}"

    

