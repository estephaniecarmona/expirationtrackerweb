from random import choices
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


CATEGORY_CHOICES = (
    ('all', 'All'),
    ('beauty', 'Beauty'),
    ('health', 'Health'),
    ('auto', 'Auto'),
    ('food', 'Food'),
    ('other','Other')
)

class ProductForm(forms.Form):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    
    # def __str__(self):
    #     return self.name


