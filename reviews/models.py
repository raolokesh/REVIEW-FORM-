from django.db import models

# Create your models here.

class ReviewData(models.Model):
    user_name = models.CharField( max_length= 50)
    review_field = models.TextField( max_length=300)
    rating_field = models.IntegerField()


    def __str__(self):
        return f"{self.user_name} {self.rating_field}"
    