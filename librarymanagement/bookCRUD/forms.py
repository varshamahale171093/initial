from dataclasses import fields
from pyexpat import model
from django import forms
from .models import bookInfo


class AddBookForm(forms.ModelForm):
    class Meta:
        model = bookInfo
        fields = ['BookName','Publication','Qty','IssueDate','subject','image'] 
         

