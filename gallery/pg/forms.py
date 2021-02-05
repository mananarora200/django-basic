from django import forms 
from .models import *
  
class UploadForm(forms.ModelForm): 
  
    class Meta: 
        model = Image_Model
        fields = ['tags', 'upload_image'] 