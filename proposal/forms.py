from os.path import splitext

from django import forms
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile

from .models import ProposalModel



class ProposalForm(forms.ModelForm):

    class Meta:
        model = ProposalModel
        exclude = ("create_on", "last_modified", "author",)

    def clean_abstract(self):
        abstract_file = self.cleaned_data.get('abstract')
        if abstract_file:
            # If it is a newly file, it will be an instance of "UploadedFile".
            if isinstance(abstract_file, UploadedFile):
                # Check its file format.
                discarded, file_extension = splitext(abstract_file.name)
                if file_extension != ".pdf":
                    raise ValidationError(_("This file format should be PDF."))
            return abstract_file
        else:
            raise ValidationError(_("Upload Failure."))
