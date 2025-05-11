from django.db import models

class storage(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=250)

    city=models.CharField(max_length=100)

    state=models.CharField(max_length=80)

    zip=models.IntegerField()
    email=models.EmailField(unique=True)

    web=models.URLField()
    age=models.IntegerField()

    
def __str__(self):
        return f"{self.first_name} {self.last_name}"

