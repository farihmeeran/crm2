from django.db import models

class Customer(models.Model):

    name = models.CharField(max_length=100)

    email = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    creation_date = models.DateTimeField(auto_now_add=True)

    due_date = models.DateTimeField()

    address = models.CharField(max_length=300)

    due_amount = models.CharField(max_length=50)


    def __str__(self):

        return self.name