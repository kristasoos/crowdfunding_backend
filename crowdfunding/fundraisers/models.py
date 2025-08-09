from django.db import models

# Create your models here.

# We inherited our class from the built-in models.Model class that comes with Django. This means that our new model has a bunch of incredibly useful functionality right out of the box. Django will even create a database table for us based on this model!
# Our model has a bunch of attributes: title, description, etc. Each of these is itself an instance of one of the classes that comes bundled with Django. These attributes tell Django what types of fields we want in our database table

class Fundraiser(models.Model):
    # We can pass arguments to our model's field attributes to specify extra functionality.
    # Title field cannnot be longer than 200 characters
    title=models.CharField(max_length=200)
    description=models.TextField()
    goal=models.IntegerField()
    image=models.URLField()
    is_open=models.BooleanField()
    # Date field should be automatically set with the current date when record is created. 
    date_created=models.DateTimeField(auto_now_add=True)



    
