from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from proposal.models import ProposalModel
from .forms import ReviewForm
from .models import ReviewRecordModel


def list_proposals(request):

    proposals = ProposalModel.objects.all()
    return render(request, "list_proposals.html", {'proposals': proposals})


def create_review(request, proposal_id):

    proposal = ProposalModel.objects.get(id=proposal_id)

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.proposal = proposal
            review.reviewer = request.user
            review.save()
            message = _("Thanks for your review!")
            messages.add_message(request, messages.SUCCESS, message)
            return redirect(reverse("proposal_review:list_proposals"))
    else:
        review_form = ReviewForm()
    return render(request, "create_review.html",
                  {"proposal": proposal, "review_form": review_form})


def list_reviews(request):
    reviews = ReviewRecordModel.objects.all()
    return render(request, "list_review.html", {"reviews": reviews})
