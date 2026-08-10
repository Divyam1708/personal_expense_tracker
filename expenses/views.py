from django.shortcuts import render, HttpResponse,redirect,reverse
from .models import MonthlyBudget, Expenses
from .forms import CreateMonthlyBudgetForm, CreateExpenseForm
from .forms import DayBasedExpensesGetForm
import calendar
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.db.models import Sum,Max, Min, Avg, Count

@login_required(login_url='accounts:login_user')
def home(request):
    
    
    if (request.method=='POST'):
        create_expense_form=CreateExpenseForm(request.POST, prefix='create_expense_form')
        
        if('create_expense_post_form' in request.POST):
            if(create_expense_form.is_valid()):
                print('VERY IN')
                print(create_expense_form.cleaned_data)
                create_expense_object=create_expense_form.save(commit=False,)
                create_expense_object.user=request.user
                create_expense_object.save()
                return redirect('expenses:home')
    else:
        create_expense_form=CreateExpenseForm(prefix='create_expense_form')
        
        
    if (request.method=='GET'):
        day_based_expenses_get_form=DayBasedExpensesGetForm()
        
        if ('day_based_expenses_get_form' in request.GET):
            day_based_expenses_get_form=DayBasedExpensesGetForm(request.GET)
            if(day_based_expenses_get_form.is_valid()):
                day_based_expenses_get_form_day=day_based_expenses_get_form.cleaned_data['day']
                day_based_expenses_get_form_month=day_based_expenses_get_form.cleaned_data['month']
                day_based_expenses_get_form_year=day_based_expenses_get_form.cleaned_data['year']
                url =reverse('expenses:day_based_expenses', kwargs={
                    'arg_1_day':day_based_expenses_get_form_day,
                    'arg_2_month': day_based_expenses_get_form_month,
                    'arg_3_year': day_based_expenses_get_form_year,
                })
                return redirect(url)
            
        
    today=timezone.now()
    expenses=Expenses.objects.filter(user=request.user)
    expenses_this_month=expenses.filter(date_time__month=today.month,date_time__year=today.year).order_by('-date_time')
    highest_expense=expenses_this_month.aggregate(max=Max('amount'),avg=Avg('amount'))
    
    
    return render(
        request,
        'expenses/home.html',
        context={
            
            'create_expense_form':create_expense_form,
            'day_based_expenses_get_form':day_based_expenses_get_form,
            
            'expenses':expenses_this_month,
            'highest_expense':highest_expense,
            'current_month_days': range(1,calendar.monthrange(today.year,today.month)[1]+1),
            'current_date': today,
    
        }
    )
    
    

@login_required(login_url='accounts:login_user')
def DayBasedExpenses(request,arg_1_day,arg_2_month,arg_3_year):
    
    expenses=Expenses.objects.filter(user=request.user,date_time__day=arg_1_day,date_time__month=arg_2_month,date_time__year=arg_3_year)
    return render(
        request,
        'expenses/DayBasedExpense.html',
        context={
            'expenses':expenses,
            'current_month_days': range(1,calendar.monthrange(arg_3_year,arg_2_month)[1]+1),
            'current_month': arg_2_month,
            'current_year':arg_3_year, 
        }
    )