from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'price', 'date', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
