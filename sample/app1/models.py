from django.db import models

# Create your models here.
class table(models.Model):
    name=models.TextField()
    country=models.TextField()
    city=models.TextField()
    salary=models.IntegerField()
class table1(models.Model):
    content=models.TextField(null=True)
class table2(models.Model):
    number=models.IntegerField()
    name=models.TextField()
    salary=models.IntegerField()
    country=models.TextField()
class user(models.Model):
    company=models.TextField()
    username=models.TextField()
    email=models.TextField()
    firstname=models.TextField()
    lastname=models.TextField()
    city=models.TextField()
    country=models.TextField()
    postalcode=models.TextField()
