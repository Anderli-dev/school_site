from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Employees, BlogPsychologa, Bullying, InfoPage, News


# need to be optimized, but HOW?
class EmployeesAdminForm(forms.ModelForm):
    about = forms.CharField(label="Про співробітника", widget=CKEditorUploadingWidget())

    class Meta:
        model = Employees
        fields = '__all__'


class BlogPsychologaAdminForm(forms.ModelForm):
    post = forms.CharField(label="Текст поста", widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogPsychologa
        fields = '__all__'


class NewsAdminForm(forms.ModelForm):
    post = forms.CharField(label="Текст поста", widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class BullyingForm(forms.ModelForm):
    post = forms.CharField(label="Текст поста", widget=CKEditorUploadingWidget())

    class Meta:
        model = Bullying
        fields = '__all__'


class InfoPageForm(forms.ModelForm):
    post = forms.CharField(label="Текст поста", widget=CKEditorUploadingWidget())

    class Meta:
        model = InfoPage
        fields = '__all__'
