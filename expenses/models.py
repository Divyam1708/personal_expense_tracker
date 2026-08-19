import datetime 
from decimal import Decimal
from django.utils import timezone
from django.db import models
from accounts.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from uuid import uuid4


class Expenses(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='expenses',
        null=False,
        blank=False,
    )
    
    amount=models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal(('0.01'))),
            MaxValueValidator(Decimal(('999999.99')))
            
        ],
        null=False,
        blank=False
    )
    
    date_time=models.DateTimeField(
        null=False,
        blank=False,
    )
    
    about=models.TextField(
        null=True,
        blank=True,
    )
    query_slug=models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False,
    )
    
    
class MonthlyBudget(models.Model):
    YEAR_CHOICES=[(y,y) for y in range(2020, datetime.date.today().year+4)]
    MONTH_CHOICES=[(m,m) for m in range(1,13)]
    
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='monthly_budget',
        null=False,
        blank=False,
    )
    
    year=models.CharField(
        choices=YEAR_CHOICES,
        null=False,
        blank=False
    )
    
    month=models.CharField(
        choices=MONTH_CHOICES,
        null=False,
        blank=False
    )
    
    set_on=models.DateTimeField(
        auto_now=True
    )
    
    class Meta:
        unique_together=('year','month','user')
        
class ExpensesRelatedImages(models.Model):
    expense=models.ForeignKey(
        Expenses,
        on_delete=models.CASCADE,
        null=False,
    )
    related_image=models.ImageField(
        upload_to='expense_related_images/'
    )
    date_time_create=models.DateTimeField(
        auto_now_add=True
    )
    
    