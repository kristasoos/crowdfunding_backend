from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    This can be used to add additional fields or methods specific to the application.
    """
    def __str__(self):
        # Return a string representation of the user in a specific format. 
        # Useful for logs in a human readable language
        # Self is a concept of Python 
        return self.username
    