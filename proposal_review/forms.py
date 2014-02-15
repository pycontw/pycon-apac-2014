from django import forms

from models import ReviewRecordModel


class ProposalForm(forms.ModelForm):

    class Meta:
        model = ReviewRecordModel
        exclude = ("proposal", "reviewer")
