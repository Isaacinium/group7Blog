from django.db import models

class Messages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}\'s email'

    class Meta:
        verbose_name_plural = 'Messages'