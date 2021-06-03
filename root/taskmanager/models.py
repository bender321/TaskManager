from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
        Model that adds extra attributes to default User model:
        bio, location, birt date
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'profile'


class Task(models.Model):
    """
        Model that represents task table in database.
    """
    user = models.ForeignKey(
                                User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True
                           )

    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task'
        ordering = ['completed']
