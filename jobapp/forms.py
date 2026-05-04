from django import forms
from .models import Job, JobSeeker


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'company', 'location_name', 'latitude', 'longitude']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Job Description'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'location_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. New York, NY'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
        }


class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ['name', 'email', 'phone', 'location_name', 'latitude', 'longitude', 'radius_km']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number (optional)'}),
            'location_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Brooklyn, NY'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'radius_km': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 500}),
        }

