from django import forms

from .models import ReviewRecordModel


class ReviewForm(forms.ModelForm):

    class Meta:
        model = ReviewRecordModel
        exclude = ("proposal", "reviewer")
