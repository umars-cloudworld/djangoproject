from django import forms
from .models import User
from django.core.validators import RegexValidator
from django.db.models import Q


class UserLoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        if not User.objects.filter(email=cleaned_data['email']).exists():
            forms.ValidationError("User is not Exists!!!")
        return cleaned_data


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    code = forms.CharField(required=True)
    mobile = forms.CharField(required=True, validators=[RegexValidator(
        regex=r'^[6-9]\d{9,9}$',
        message="Phone number must be entered in the format '9087654321'. Up to 10 digits allowed."
      )])
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'code', 'mobile', 'password')

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        if User.objects.filter(email=cleaned_data['email']).exists():
            raise forms.ValidationError("Email Already Exists !!!")
        if 'mobile' in cleaned_data and User.objects.filter(mobile=cleaned_data['mobile']).exists():
            raise forms.ValidationError("mobile Already Exists !!!")
        return cleaned_data


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    code = forms.CharField(required=False)
    mobile = forms.CharField(required=False, validators=[RegexValidator(
        regex=r'^\d{6,15}$',
        message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
      )])
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'code', 'mobile', 'profile_image')

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        return cleaned_data


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email', )

    def clean(self):
        cleaned_data = super(ForgetPasswordForm, self).clean()
        if not User.objects.filter(email=cleaned_data['email']).exists():
            forms.ValidationError("Email Not Exists")
        return cleaned_data

