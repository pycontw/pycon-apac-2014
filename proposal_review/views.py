from django.shortcuts import render

from proposal.models import ProposalModel


def list_proposals(request):

    proposals = ProposalModel.objects.all()
    return render(request, "list_proposals.html", {'proposals': proposals})


def create_review(request, proposal_id):

    proposal = ProposalModel.objects.get(id=proposal_id)
    return render(request, "create_review.html", {"proposal": proposal})
