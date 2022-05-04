from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import ClearableFileInput

from main.models import EnterSchool


class MyClearableFileInput(ClearableFileInput):
    initial_text = 'Документ наразі'


class TextArea(forms.ModelForm):

    if EnterSchool.objects.filter(pk=1).exists():
        def __init__(self, *args, **kwargs):
            super(TextArea, self).__init__(*args, **kwargs)
            self.fields['content'].initial = EnterSchool.objects.get(pk=1).content
            self.fields['document'].initial = EnterSchool.objects.get(pk=1).document

    content = forms.CharField(
        widget=CKEditorWidget(),
        label="Контент"
    )
    document = forms.FileField(
        widget=MyClearableFileInput(),
        label="Документ",
        allow_empty_file=True,
    )

    class Meta:
        model = EnterSchool
        fields = "__all__"
