from django.db import models

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200, null=False)
    cooked_date = models.DateTimeField('data cooked')