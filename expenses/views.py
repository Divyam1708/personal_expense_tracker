from django.shortcuts import render, HttpResponse,redirect,reverse
from .models import MonthlyBudget, Expenses, ExpensesRelatedImages
from .forms import CreateMonthlyBudgetForm, CreateExpenseForm, ExpenseRelatedImageForm
from .forms import ExpenseDetailEditForm
from .forms import DayBasedExpensesGetForm, MonthBasedExpensesGetForm
import calendar
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.db.models import Sum,Max, Min, Avg, Count

@login_required
def home(request):
    
    
    # POST FORM HANDLING
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
        
        
    # GET FORM HANDLING
    if (request.method=='GET'):
        day_based_expenses_get_form=DayBasedExpensesGetForm()
        month_based_expenses_get_form=MonthBasedExpensesGetForm()
        
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
            
            
        elif ('month_based_expenses_get_form' in request.GET):
            month_based_expenses_get_form=MonthBasedExpensesGetForm(request.GET)
            if(month_based_expenses_get_form.is_valid()):
                month_based_expenses_get_form_month=month_based_expenses_get_form.cleaned_data['month']
                month_based_expenses_get_form_year=month_based_expenses_get_form.cleaned_data['year']
                url =reverse('expenses:month_based_expenses', kwargs={
                    'arg_1_month': month_based_expenses_get_form_month,
                    'arg_2_year': month_based_expenses_get_form_year,
                })
                return redirect(url)
                
                
                
        
    today=timezone.now()
    expenses=Expenses.objects.filter(user=request.user)
    expenses_this_month=expenses.filter(date_time__month=today.month,date_time__year=today.year).order_by('-date_time')
    highest_expense=expenses_this_month.aggregate(max=Max('amount'),avg=Avg('amount'))
    highest_expense_date_time=expenses_this_month.filter(amount=highest_expense['max']).first()
    
    
    return render(
        request,
        'expenses/home.html',
        context={
            
            'create_expense_form':create_expense_form,
            'day_based_expenses_get_form':day_based_expenses_get_form,
            'month_based_expenses_get_form':month_based_expenses_get_form,
            
            'expenses':expenses_this_month,
            'highest_expense':highest_expense['max'],
            'highest_expense_date_time':highest_expense_date_time,
            'current_month_days': range(1,calendar.monthrange(today.year,today.month)[1]+1),
            'current_date': today,
    
        }
    )
    
    

@login_required
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
    
    
    
@login_required
def MonthBasedExpenses(request,arg_1_month,arg_2_year):
    
    expenses=Expenses.objects.filter(user=request.user,date_time__month=arg_1_month,date_time__year=arg_2_year)
    calculated_expenses=expenses.aggregate(max=Max('amount'),min=Min('amount'),avg=Avg('amount'),sum=Sum('amount'),count=Count('amount'))
    maximum_expense_current_month=calculated_expenses['max']
    minimum_expense_current_month=calculated_expenses['min']
    average_expense_current_month=calculated_expenses['avg']
    total_expense_current_month=calculated_expenses['sum']
    number_of_times_expensed=calculated_expenses['count']
    
    return render(
        request,
        'expenses/MonthBasedExpense.html',
        context={
            'expenses':expenses,
            'current_month_days': range(1,calendar.monthrange(arg_2_year,arg_1_month)[1]+1),
            'current_month': arg_1_month,
            'current_year':arg_2_year, 
            'maximum_expense':maximum_expense_current_month,
            'minimum_expense':minimum_expense_current_month,
            'average_expense':average_expense_current_month,
            'total_expense':total_expense_current_month,
            'number_of_expenses':number_of_times_expensed,
        }
    )
    
@login_required
def ExpenseDetail(request,arg_1_expense_query_slug):
    
    try:
        expense=Expenses.objects.get(query_slug=arg_1_expense_query_slug, user=request.user)
    except Expenses.DoesNotExist as e:
        return render(
            request,
            'base/Error_1.html',
            context={
                'message':f'{e} Please do not try to Violate.'
            }
        )
        
    if (request.method=='POST'):
        if('expense_edit_detail_form' in request.POST):
            expense_detail_edit_form=ExpenseDetailEditForm(request.POST, instance=expense)
            if(expense_detail_edit_form.is_valid()):
                expense.save()
                url=reverse(
                    'expenses:expense_detail',
                    kwargs={
                        'arg_1_expense_query_slug':arg_1_expense_query_slug,
                    }
                )
                return  redirect(url)
    
    else:
        expense_detail_edit_form=ExpenseDetailEditForm(instance=expense)
            
        
    expense_related_images=ExpensesRelatedImages.objects.filter(expense=expense)
    if request.method =='POST':
        if('expense_related_image_form' in request.POST):
            expense_related_image_form=ExpenseRelatedImageForm(request.POST, request.FILES)
            if(expense_related_image_form.is_valid()):
                ex_re_img_obj=expense_related_image_form.save(commit=False)
                ex_re_img_obj.expense=expense
                ex_re_img_obj.save()
                url=reverse(
                    'expenses:expense_detail',
                    kwargs={
                        'arg_1_expense_query_slug':arg_1_expense_query_slug,
                    }
                )
                return redirect(url)
                
    else:
        expense_related_image_form=ExpenseRelatedImageForm()
        
        
    return render(
        request,
        'expenses/ExpenseDetail.html',
        context={
            'expense':expense,
            
            'expense_detail_edit_form':expense_detail_edit_form,
            'expense_related_image_form':expense_related_image_form,
            
            'expense_related_images':expense_related_images,
            
        }
    )