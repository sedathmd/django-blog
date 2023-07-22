from django.db import models

class DateAbstractModel(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True