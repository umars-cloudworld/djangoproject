from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.template.defaultfilters import slugify


class ContactUsForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    name = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.TextInput())

    class Meta:
        model = ContactUs
        fields = ('email', 'subject', 'name', 'message')

    def clean(self):
        cleaned_data = super(ContactUsForm, self).clean()
        return cleaned_data


class NewsLetterForm(forms.Form):
    email = forms.EmailField(required=True)

    class Meta:
        model = NewsLetter
        fields = ('email', )

    def clean(self):
        cleaned_data = super(NewsLetterForm, self).clean()
        return cleaned_data


class MapForm(forms.ModelForm):

    class Meta:
        model = Map
        fields = '__all__'


class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Projects
        fields = '__all__'

    def clean(self):
        cleaned_data = super(ProjectsForm, self).clean()
        if 'slug' not in cleaned_data or not cleaned_data['slug']:
            cleaned_data['slug'] = str(slugify(cleaned_data['name']))
        return cleaned_data


class UserModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class PricingForm(forms.ModelForm):
    project = UserModelChoiceField(queryset=Projects.objects.all(), required=True)
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Pricing
        fields = ('project', 'title', 'description', 'icon_class' , 'is_active')

    def clean(self):
        cleaned_data = super(PricingForm, self).clean()
        return cleaned_data


class OurProjectsForm(forms.ModelForm):
    title = forms.CharField(required=True)
    image = forms.FileField(required=True)
    description = forms.CharField(required=True, widget=CKEditorWidget())
    is_active = forms.BooleanField(initial=True)

    class Meta:
        model = Pricing
        fields = ('title', 'image', 'description', 'is_active')

    def clean(self):
        cleaned_data = super(OurProjectsForm, self).clean()
        return cleaned_data
