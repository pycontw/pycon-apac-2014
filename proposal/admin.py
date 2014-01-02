from django.contrib import admin
from models import ProposalModel
from forms import ProposalForm


class ProposalModelAdmin(admin.ModelAdmin):
    list_display = ("id", "create_on", "last_modified", 'title', 'author',
                    'speech_type', "language", "audience_level", "description",
                    "additional_info")

    list_filter = ('language', 'audience_level', 'speech_type', 'author')

    form = ProposalForm


admin.site.register(ProposalModel, ProposalModelAdmin)
