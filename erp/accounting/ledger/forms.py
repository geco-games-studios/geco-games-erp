from django import forms
from .models import LedgerAccount, Transaction, TransactionEntry

class LedgerAccountForm(forms.ModelForm):
    class Meta:
        model = LedgerAccount
        fields = ['name', 'description', 'balance',]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'border-2 border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:border-blue-500',
                'placeholder': f'Enter {field.label}'
            })
        

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'description', 'reference']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'border-2 border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:border-blue-500',
                'placeholder': f'Enter {field.label}'
            })
        
        # Set the date input type and custom attributes for date formatting
        self.fields['date'].widget.attrs.update({
            'type': 'date',  # Use the HTML5 date input
            'class': 'border-2 border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:border-blue-500',  # Keep the existing styles
        })

class TransactionEntryForm(forms.ModelForm):
    class Meta:
        model = TransactionEntry
        fields = ['transaction', 'account', 'title', 'description', 'debit', 'credit']

    def __init__(self, *args, **kwargs):
        transaction = kwargs.pop('transaction', None)
        super().__init__(*args, **kwargs)
        if transaction:
            self.fields['transaction'].initial = transaction
            self.fields['transaction'].widget = forms.HiddenInput()
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'border-2 border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:border-blue-500',
                'placeholder': f'Enter {field.label}'
            })