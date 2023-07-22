from django.db import models

class ContactModel(models.Model):
    email = models.EmailField(max_length=100)
    full_name = models.CharField(max_length=100)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.email