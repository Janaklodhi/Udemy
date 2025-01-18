# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.db import models

# class User(AbstractUser):
#     # Add unique related_name to avoid conflicts
#     groups = models.ManyToManyField(
#         Group,
#         related_name="custom_user_set",  # Change this to avoid conflict
#         blank=True,
#         help_text="The groups this user belongs to.",
#         verbose_name="groups",
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name="custom_user_permissions",  # Change this to avoid conflict
#         blank=True,
#         help_text="Specific permissions for this user.",
#         verbose_name="user permissions",
#     )



from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom User model with custom username field.
    """
    username = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Username",
        help_text="A unique identifier for the user."
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email Address",
        help_text="A unique email address for the user."
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name="custom_user_set",  # Custom related_name
        blank=True,
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="custom_user_permissions",  # Custom related_name
        blank=True,
        verbose_name="user permissions",
    )

    # Override REQUIRED_FIELDS for custom username
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'  # Set custom username field

    def __str__(self):
        return self.username
