from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Business(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Businesses"

class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Ledger(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Head(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Mode(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    DR_CR_CHOICES = [
        ('Dr', 'Debit'),
        ('Cr', 'Credit')
    ]
    GST_CHOICES = [
        ('With GST', 'With GST'),
        ('Without GST', 'Without GST')
    ]

    transaction_date = models.DateField()
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE)
    head = models.ForeignKey(Head, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    dr_or_cr = models.CharField(max_length=2, choices=DR_CR_CHOICES)
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE)
    discount_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    gst = models.CharField(max_length=11, choices=GST_CHOICES)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.transaction_date} - {self.business.name} - {self.amount}"