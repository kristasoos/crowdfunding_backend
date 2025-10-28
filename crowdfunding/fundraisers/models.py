from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# We inherited our class from the built-in models.Model class that comes with Django. This means that our new model has a bunch of incredibly useful functionality right out of the box. Django will even create a database table for us based on this model!
# Our model has a bunch of attributes: title, description, etc. Each of these is itself an instance of one of the classes that comes bundled with Django. These attributes tell Django what types of fields we want in our database table

class Fundraiser(models.Model):
    # We can pass arguments to our model's field attributes to specify extra functionality.
    # Title field cannnot be longer than 200 characters
    title=models.CharField(max_length=200)
    description=models.TextField()
    goal=models.IntegerField()
    # URL field is for validation. 
    image=models.URLField()
    is_open=models.BooleanField()
    # Date field should be automatically set with the current date when record is created. 
    # Automatically add the current time and date to DB.
    date_created=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(
        get_user_model(),
        related_name="owned_fundraisers",
        on_delete=models.CASCADE
    )


class Pledge(models.Model):
    # Info to this class comes from the database table drawing. If we add more firlds to the table, we also need t add them here. 
    amount=models.IntegerField()
    comment=models.CharField(max_length=200)
    anonymous=models.BooleanField()
    fundraiser=models.ForeignKey(
        # in our case it needs to match the class name above
        "Fundraiser",
        # Tells djando to add extra information to Fundraiser. name of the property to create.
        related_name="pledges",
        # on delete means that if the fundraiser is deleted, all pledges related to it will also be deleted.
        on_delete=models.CASCADE
    )
    supporter=models.ForeignKey(
        get_user_model(),
        related_name="pledges",
        on_delete=models.CASCADE
    )



   




    
