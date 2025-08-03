from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Expense
from django.db.models import Sum
from datetime import datetime
from collections import defaultdict
import json
from .forms import ExpenseForm


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "expenses/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def home(request):
    return render(request, "expenses/home.html")


@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expenses')
    else:
        form = ExpenseForm()

    return render(request, 'expenses/add_expense.html', {'form': form})


@login_required
def expenses_view(request):
    now = datetime.now()
    user_expenses = Expense.objects.filter(user=request.user).order_by("-date")

    # Calculate monthly total
    monthly_expenses = user_expenses.filter(
        date__month=now.month, date__year=now.year
    )
    monthly_total = monthly_expenses.aggregate(Sum("price"))["price__sum"] or 0

    # Calculate yearly total
    yearly_expenses = user_expenses.filter(date__year=now.year)
    yearly_total = yearly_expenses.aggregate(Sum("price"))["price__sum"] or 0

    # Category-wise breakdown
    category_data = defaultdict(float)
    for exp in user_expenses:
        category_data[exp.category] += float(exp.price)

    context = {
        "expenses": user_expenses,
        "monthly_total": monthly_total,
        "yearly_total": yearly_total,
        "category_labels": json.dumps(list(category_data.keys())),
        "category_values": json.dumps(list(category_data.values())),
    }
    return render(request, "expenses/expense_list.html", context)


@login_required
def monthly_expenses(request):
    expenses = []
    total = 0
    selected_month = None
    selected_year = None
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    years = list(range(2020, datetime.now().year + 1))

    if request.method == 'POST':
        selected_month = int(request.POST.get('month'))
        selected_year = int(request.POST.get('year'))
        expenses = Expense.objects.filter(
            user=request.user,
            date__month=selected_month,
            date__year=selected_year
        )
        total = expenses.aggregate(Sum('price'))['price__sum'] or 0

    context = {
        'expenses': expenses,
        'total': total,
        'selected_month': selected_month,
        'selected_year': selected_year,
        'months': months,
        'years': years,
    }
    return render(request, 'expenses/monthly_expense.html', context)
