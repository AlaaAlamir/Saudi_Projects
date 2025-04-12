from django import forms
from django.forms import ModelForm
from .models import FutureVision

class FutureVisionForm(ModelForm):
    class Meta:
        model = FutureVision
        fields = {'name','specialization','vision_text'}