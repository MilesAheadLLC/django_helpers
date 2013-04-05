from django.db import models
from django.utils.timezone import now

class CreateUpdateModel(models.Model):
    """
     Abstract model class that adds created_at and updated_at fields
    """
    created_at = models.DateTimeField(auto_now_add=True,default=now)
    updated_at = models.DateTimeField(auto_now=True,default=now)

    class Meta:
        abstract = True
