from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from djongo import models


LOGOS_FOLDER_ROOT = "logos"


class Project(models.Model):
    """Ess project model class."""
    company_name = models.CharField(max_length=50)
    logo = models.FileField(upload_to=LOGOS_FOLDER_ROOT, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    owner_name = models.CharField(max_length=50)

    # TODO: This could be an enumeration choices
    sector = models.CharField(max_length=50)

    # FIXME: This should be an enumeration choices with available countries
    country = models.CharField(max_length=50)

    users = models.ArrayReferenceField(User, on_delete=models.CASCADE, null=True, blank=True)
    tasks = models.ArrayReferenceField("Task", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"Project {self.id} {self.company_name} ({self.owner_name})"
