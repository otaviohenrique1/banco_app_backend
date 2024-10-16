from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Account(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='account')
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Account {self.account_number} - {self.customer.first_name} {self.customer.last_name}"
