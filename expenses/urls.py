from django.urls import include, path
from expenses import views
app_name='expenses'

urlpatterns = [
    path('',views.home,name='home'),
    path('day-based-expense/<int:arg_1_day>-<int:arg_2_month>-<int:arg_3_year>',views.DayBasedExpenses,name='day_based_expenses'),
    path('month-based-expense/<int:arg_1_month>-<int:arg_2_year>',views.MonthBasedExpenses,name='month_based_expenses'),
    path('see_detail/<slug:arg_1_expense_query_slug>', views.ExpenseDetail,name='expense_detail'),   
    path('delete-related-image/<int:arg_1_image_id>', views.DeleteExpenseRelatedImage, name='delete-expense-related-image'),
    path('delete-expense/<slug:arg_1_expense_query_slug>',views.DeleteExpense, name='delete-expense')
]
