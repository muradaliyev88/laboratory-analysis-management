from django import forms
from polls.models import *
from django.contrib import admin



class QR_Form(forms.ModelForm):
	
	class Meta:
		model = QR
		fields = '__all__'



class Barcode_Form(forms.ModelForm):
	
	class Meta:
		model = Barcode
		fields = '__all__'



admin.site.register(Barcode)
admin.site.register(QR)




