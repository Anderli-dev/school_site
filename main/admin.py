from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import *

admin.site.site_title = 'Адміністрування сайту НВК "Турбота"'
admin.site.site_header = 'Адміністрування сайту НВК "Турбота"'


class DocumentFilesAdmin(admin.StackedInline):
    model = DocumentFiles
    verbose_name = "Документ"
    verbose_name_plural = "Документи"
    extra = 0
    min_num = 1


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    inlines = [DocumentFilesAdmin]
    exclude = ["slug"]

    class Meta:
        model = Document


class EmployeesAdminForm(forms.ModelForm):
    about = forms.CharField(label="Про співробітника", widget=CKEditorUploadingWidget())

    class Meta:
        model = Employees
        fields = '__all__'


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    form = EmployeesAdminForm


class FinanceFilesAdmin(admin.StackedInline):
    model = FinanceFiles


@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    inlines = [FinanceFilesAdmin]
    exclude = ["slug"]

    class Meta:
        model = Finance


class BlogPsychologaAdminForm(forms.ModelForm):
    post = forms.CharField(label="Текст поста", widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogPsychologa
        fields = '__all__'


@admin.register(BlogPsychologa)
class BlogPsychologaAdmin(admin.ModelAdmin):
    form = BlogPsychologaAdminForm
    exclude = ["slug"]


class NewsAdminForm(forms.ModelForm):
    post = forms.CharField(label="Текст поста", widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    exclude = ["slug"]


class BullyingForm(forms.ModelForm):
    post = forms.CharField(label="Текст поста", widget=CKEditorUploadingWidget())

    class Meta:
        model = Bullying
        fields = '__all__'


@admin.register(Bullying)
class BullyingAdmin(admin.ModelAdmin):
    form = BullyingForm
    exclude = ["slug"]


admin.site.register(Vacancy)


class DistanceStudyForm(forms.ModelForm):
    post = forms.CharField(label="Текст поста", widget=CKEditorUploadingWidget())

    class Meta:
        model = DistanceStudy
        fields = '__all__'


@admin.register(DistanceStudy)
class BullyingAdmin(admin.ModelAdmin):
    form = DistanceStudyForm
    exclude = ["slug"]
