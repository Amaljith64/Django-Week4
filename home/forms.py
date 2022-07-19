from cProfile import label
from datetime import date

from tkinter import Widget
from django import forms
from . models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class Book (forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'bdate': DateInput(),
        }

        labels= {
            'pname':"Patient Name",
            'pnumber':"Patient's Phone Number",
            'paddress':"Pateint's Address",
            'pemail':"Patient's Email ID",
            'doc_name':"Doctor's Name",
            'bdate':'Booking Date'
              }

