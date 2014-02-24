from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from proposal.models import ProposalModel

from conweb.utils import require_group
from .forms import ReviewForm
from .models import ReviewRecordModel


REVIEWER_GROUP_NAME = getattr(settings, "REVIEWER_GROUP_NAME", "Reviewer")


@login_required
@require_group(REVIEWER_GROUP_NAME)
def list_proposals(request):

    proposals = ProposalModel.objects.annotate(Avg('reviewrecordmodel__rank'))

    return render(request, "list_proposals.html", {'proposals': proposals})


@login_required
@require_group(REVIEWER_GROUP_NAME)
def do_review(request, proposal_id):

    proposal = ProposalModel.objects.get(id=proposal_id)

    reviews = ReviewRecordModel.objects.filter(proposal=proposal).exclude(reviewer=request.user)

    average_rank = ReviewRecordModel.objects.filter(proposal=proposal).aggregate(Avg('rank')).get("rank__avg", None)

    review, create = ReviewRecordModel.objects.get_or_create(proposal=proposal,
                                                             reviewer=request.user)

    if request.method == "POST":

        review_form = ReviewForm(request.POST, instance=review)

        if review_form.is_valid():
            review.save()
            message = _("Thanks for your review!")
            messages.add_message(request, messages.SUCCESS, message)
            return redirect(reverse("proposal_review:list_proposals"))
    else:
        try:
            review = ReviewRecordModel.objects.get(proposal=proposal, reviewer=request.user)
        except:
            review = None
        review_form = ReviewForm(instance=review)
    return render(request, "create_review.html",
                  {"proposal": proposal, "review_form": review_form,
                   "reviews": reviews, "average_rank": average_rank})


@login_required
@require_group(REVIEWER_GROUP_NAME)
def list_reviews(request, me=False):
    if me:
        reviews = ReviewRecordModel.objects.filter(reviewer=request.user)
    else:
        reviews = ReviewRecordModel.objects.all()
    return render(request, "list_reviews.html", {"reviews": reviews})
