from django.db import models

class InvestingModel(models.Model):
    title = models.TextField()
    content = models.TextField()
