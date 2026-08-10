from expenses import models
from django import forms
import datetime
from django.utils import timezone
class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model=models.Expenses
        exclude=['user']
        widgets={
            'date_time':forms.DateTimeInput(
                attrs={
                    'type':'datetime-local',
                }
            ),
            'amount':forms.NumberInput(
                attrs={
                    'type':'number',
                    'min':'0',
                    'step':'0.5',
                    'placeholder':'1205.5'
                }
            ),
            'about':forms.Textarea(
                attrs={
                    'cols':"24",
                    'rows':"4"
                }
            )
            
        }


class CreateMonthlyBudgetForm(forms.ModelForm):
    class Meta:
        model=models.MonthlyBudget
        exclude=['user']



class DayBasedExpensesGetForm(forms.Form):
    YEAR_CHOICES=[(y,y) for y in range(2020, datetime.date.today().year+4)]
    MONTH_CHOICES=[(m,m) for m in range(1,13)]
    DAY_CHOICE=[(d,d) for d in range(1,32)]
    
    day=forms.ChoiceField(choices=DAY_CHOICE,initial=timezone.now().day)
    month=forms.ChoiceField(choices=MONTH_CHOICES,initial=timezone.now().month)
    year=forms.ChoiceField(choices=YEAR_CHOICES, initial=timezone.now().year)
    
    