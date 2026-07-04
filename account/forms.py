from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CompanyProfile
from .models import Resume
class CandidateRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class CompanyRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    company_name = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ['username', 'email']

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file')

        if file:
            if not file.name.endswith('.pdf'):
                raise forms.ValidationError("Faqat PDF formatidagi fayllarni yuklash mumkin!")

            max_size = 5 * 1024 * 1024
            if file.size > max_size:
                raise forms.ValidationError("Fayl hajmi 5MB oshmasligi kerak!")

        return file