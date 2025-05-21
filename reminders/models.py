from django.db import models

# Create your models here.
class Reminder(models.Model):
    REMINDER_METHODS = [
        ('SMS', 'SMS'),
        ('EMAIL', 'Email'),
    ]

    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    reminder_method = models.CharField(max_length=10, choices=REMINDER_METHODS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reminder_method} @ {self.date} {self.time}"