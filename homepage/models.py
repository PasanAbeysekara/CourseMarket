from django.db import models


# Create your models here.
class Course(models.Model):
    CATEGORY_CHOICES = (
        ("Django", "Django"),
        ("Angular", "Angular"),
        ("ASP.NET", "ASP.NET")
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    uploaded_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name[:10] + '-' + self.category
