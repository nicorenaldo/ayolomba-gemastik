from django import forms
from django.contrib.auth.models import User
from .models import Lomba
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from ckeditor.widgets import CKEditorWidget

class SubmitForm(forms.ModelForm):
    
    class Meta:
        model = Lomba
        exclude = ['visited','created','active','slug','owner_email','owner']
        widgets = {
            'deadline':DatePickerInput(),
            'tanggalpelaksanaan':DatePickerInput(),
            'image': forms.ClearableFileInput(),
            'description' : CKEditorWidget()
        }
        labels = {
        "name": "Nama Lomba"
        }

    def clean_tags(self):
        tn = self.cleaned_data.get('tags', [])
        if len(tn) > 30:
            raise ValidationError(_('Invalid value'), code='invalid')
        return tn

    def __init__(self, *args, **kwargs):
        super(SubmitForm, self).__init__(*args, **kwargs)
        self.fields['description'].strip = False

class BookmarkForm(forms.Form):
    lomba = forms.ModelChoiceField(queryset=Lomba.objects.all())

