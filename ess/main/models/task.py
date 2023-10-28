from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from djongo import models



class Task(models.Model):
    """Ess project task model class."""
    name = models.CharField(max_length=50)
    assigned_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_("User responsible of the task"),
    )
    # Planning information
    start_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(
        help_text=_("Task deadline"),
        null=True, blank=True
    )
