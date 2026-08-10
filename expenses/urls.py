from django.urls import include, path
from expenses import views

app_name='expenses'

urlpatterns = [
    path('',views.home,name='home'),
    path('<int:arg_1_day>-<int:arg_2_month>-<int:arg_3_year>',views.DayBasedExpenses,name='day_based_expenses'),
    
]
