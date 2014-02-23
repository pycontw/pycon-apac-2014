from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import ReviewRecordModel


class ReviewForm(forms.ModelForm):

    class Meta:
        model = ReviewRecordModel
        exclude = ("proposal", "reviewer")
        widgets = {'rank': forms.RadioSelect}

    def clean_rank(self):
        data = self.cleaned_data['rank']
        if data > 5 or data < 0:
            raise forms.ValidationError(_("The value of rank should be between zero and five."))
        return data
