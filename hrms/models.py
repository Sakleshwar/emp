from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    designation = models.CharField(max_length=20)
    address = models.TextField()

class Paystub1(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    gross_earnings = models.DecimalField(max_digits=10, decimal_places=2)
    overtime_earnings = models.DecimalField(max_digits=10, decimal_places=2)
    pre_tax_deductions = models.DecimalField(max_digits=10, decimal_places=2)
    federal_income_tax = models.DecimalField(max_digits=10, decimal_places=2)
    state_income_tax = models.DecimalField(max_digits=10, decimal_places=2)
    post_tax_deductions = models.DecimalField(max_digits=10, decimal_places=2)
    employer_contribution = models.DecimalField(max_digits=10, decimal_places=2)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)

class TimeOffRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    is_approved = models.BooleanField(default=False)


class Policy(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

