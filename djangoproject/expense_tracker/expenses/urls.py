from django.contrib import admin
from django.urls import path
from expenses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_expense, name='add_expense'),
    path('monthly/', views.monthly_expenses, name='monthly_expenses'),
    path('expenses/', views.expenses_view, name='expenses'),
]
