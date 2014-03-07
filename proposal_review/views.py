from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Avg, Sum, Count

from proposal.models import ProposalModel

from conweb.utils import require_group
from .forms import ReviewForm, ProposalResultForm
from .models import ReviewRecordModel, ProposalResultModel


REVIEWER_GROUP_NAME = getattr(settings, "REVIEWER_GROUP_NAME", "Reviewer")
reviewer_admins = getattr(settings, "REVIEWER_ADMINS", [])


def _is_review_admin(request):
    return request.user.username in ['admin'] + reviewer_admins


@login_required
@require_group(REVIEWER_GROUP_NAME)
def list_proposals(request):

    proposals = (ProposalModel.objects
                 .annotate(rank_avg=Avg('reviewrecordmodel__rank'))
                 .annotate(rank_sum=Sum('reviewrecordmodel__rank'))
                 .annotate(reviewers_amount=Count('reviewrecordmodel__rank')))
    proposals = sorted(proposals, key=lambda x: x.id, reverse=True)

    type_counts = {
        type_name: len([p for p in proposals if p.speech_type == speech_type])
        for speech_type, type_name in ProposalModel.SPEECH_TYPE_CHOICES
    }
    statistic = {
        "total": len(proposals),
        "type_counts": type_counts
    }
    is_reviewer_admin = _is_review_admin(request)
    return render(request, "list_proposals.html",
                  {'proposals': proposals, 'statistic': statistic,
                   'is_reviewer_admin': is_reviewer_admin})


@login_required
@require_group(REVIEWER_GROUP_NAME)
def do_review(request, proposal_id):

    proposal = ProposalModel.objects.get(id=proposal_id)
    is_reviewer_admin = _is_review_admin(request)
    if proposal.author == request.user and not is_reviewer_admin:
        message = _("Thanks for your curiosity!")
        messages.add_message(request, messages.WARNING, message)
        return redirect(reverse("proposal_review:list_proposals"))

    reviews = ReviewRecordModel.objects.filter(proposal=proposal) \
        .exclude(reviewer=request.user)

    average_rank = ReviewRecordModel.objects.filter(proposal=proposal) \
        .aggregate(Avg('rank')).get("rank__avg", None)

    if request.method == "POST":

        review, create = ReviewRecordModel.objects.get_or_create(
            proposal=proposal,
            reviewer=request.user
        )
        review_form = ReviewForm(request.POST, instance=review)

        if review_form.is_valid():
            review.save()
            message = _("Thanks for your review!")
            messages.add_message(request, messages.SUCCESS, message)
            return redirect(reverse("proposal_review:list_proposals"))
    else:
        try:
            review = ReviewRecordModel.objects \
                .get(proposal=proposal, reviewer=request.user)
        except ReviewRecordModel.DoesNotExist:
            review = None
        review_form = ReviewForm(instance=review)

        if is_reviewer_admin:
            # Create at first time.
            proposal_result, create = ProposalResultModel.objects \
                .get_or_create(proposal=proposal)
            result_form = ProposalResultForm(instance=proposal_result)
        else:
            proposal_result = None
            result_form = None
    return render(request, "create_review.html",
                  {"proposal": proposal, "review_form": review_form,
                   "reviews": reviews, "average_rank": average_rank,
                   "result_form": result_form,
                   "is_reviewer_admin": is_reviewer_admin,
                   "proposal_result": proposal_result})


@login_required
@require_group(REVIEWER_GROUP_NAME)
def list_reviews(request, me=False):
    if me:
        reviews = ReviewRecordModel.objects.filter(reviewer=request.user)
    else:
        reviews = ReviewRecordModel.objects.all()
    return render(request, "list_reviews.html", {"reviews": reviews})


@login_required
@require_POST
def make_decision(request, proposal_id):

    is_reviewer_admin = _is_review_admin(request)

    if not is_reviewer_admin:
        raise PermissionDenied("Invalid user.")

    try:
        proposal_result = ProposalResultModel.objects \
            .get(proposal_id=proposal_id)
    except ReviewRecordModel.DoesNotExist:
        proposal_result = None

    result_form = ProposalResultForm(request.POST, instance=proposal_result)
    result = result_form.save(commit=False)
    result.referee = request.user
    result.save()

    return redirect(reverse("proposal_review:do_review", args=(proposal_id,)))
