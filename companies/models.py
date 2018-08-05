from django.db import models


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(unique=True, max_length=100, blank=False, null=False)


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    review = models.TextField(blank=False, null=False)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField()
    employee_position = models.CharField(max_length=50, blank=False, null=False)
    employee = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)



