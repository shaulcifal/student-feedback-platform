from django.db import models
# from djangoratings.fields import RatingField

from account.models import (
    Student,
)

# Create your models here.

class Feedback(models.Model) :

    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    
    content = models.TextField(max_length=255, blank=False)
    # course_rating = RatingField(range=10)
    course_rating = models.CharField(max_length=255, choices=RATING_CHOICES, null=False)
    course = models.CharField(max_length=255, null=False)

    is_draft = models.BooleanField(default = False)


    upvotes = models.IntegerField(default = 0)
    votes = models.IntegerField(default = 0)
    downvotes = models.IntegerField(default = 0)

    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL) # set_null or cascade

    date_submitted = models.DateTimeField(verbose_name = "date_submitted", auto_now_add = True)
    


class TestModel(models.Model) :
    name = models.CharField(max_length=256)


    def __str__(self) :
        return self.name