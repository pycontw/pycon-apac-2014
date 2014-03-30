# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from proposal.models import ProposalModel


def list_speakers(request):

    speakers = {}

    author_of_accept_proposals = ProposalModel.objects.filter(result__decision=1) \
        .values_list("author", flat=True)
    speakers = User.objects.filter(id__in=author_of_accept_proposals)

    return render(request, "list_speakers.html", {"speakers": speakers})
