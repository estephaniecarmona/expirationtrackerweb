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

EXPIRATION_DATES = (
    ('newest', 'Newest'),
    ('oldest', 'Oldest')
)

EXPIRED_PRODUCT = (
    ('expired', 'Expired'),
    ('notexpired', 'Not Expired'),
    ('all', 'All')
)
class ProductForm(forms.Form):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    
    expiration = forms.ChoiceField(choices=EXPIRATION_DATES)

    expired_products = forms.ChoiceField(choices=EXPIRED_PRODUCT)

    
