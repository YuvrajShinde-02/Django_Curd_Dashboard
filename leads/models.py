from django.db import models

# Create your models here.
class Lead(models.Model):
    SOURCE_CHOICES = [
        ("website", "Website"),
        ("referral", "Referral"),
        ("ads", "Ads"),
        ("api", "API Import"),
        ("other", "Other"),
    ]
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default="other")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"
