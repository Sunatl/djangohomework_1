from django import forms
from .models import *

class Tasksform(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ("name","due_date","imeges","status","company","description","user")
        
        
        
class Companyform(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("name","imeges")
        