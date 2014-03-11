from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import ReviewRecordModel, ProposalResultModel


class ReviewForm(forms.ModelForm):

    class Meta:
        model = ReviewRecordModel
        exclude = ("proposal", "reviewer")
        widgets = {'rank': forms.RadioSelect}

    def clean_rank(self):
        data = self.cleaned_data['rank']
        if data > 3 or data < -3:
            raise forms.ValidationError(_("The value of rank should be between 3 and -3."))
        return data


class ProposalResultForm(forms.ModelForm):

    class Meta:
        model = ProposalResultModel
        fields = ("decision",)
        widgets = {'decision': forms.RadioSelect}
