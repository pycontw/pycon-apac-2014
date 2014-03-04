from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.exceptions import PermissionDenied

from .forms import ProposalForm, AbstractFileForm
from .models import ProposalModel, AbstractFile


@login_required
def create_proposal(request):

    if not settings.CALL_FOR_PROPOSAL:
        raise PermissionDenied("Time is up.")

    if request.method == "POST":

        proposal_form = ProposalForm(request.POST, request.FILES)

        if proposal_form.is_valid():
            proposal = proposal_form.save(commit=False)
            proposal.author = request.user
            proposal.save()
            message = _("Thanks for your submission!")
            messages.add_message(request, messages.SUCCESS, message)
            return redirect(reverse("proposal:list"))
        else:
            return render(request, "proposal/create.html",
                          {"proposal_form": proposal_form})
    else:

        proposal_form = ProposalForm()

        return render(request, "proposal/create.html",
                      {"proposal_form": proposal_form})


@login_required
def list_proposal(request):

    my_proposal = ProposalModel.objects.filter(author=request.user)
    return render(request, "proposal/list.html",
                  {"my_proposal": my_proposal,
                   "upload_abstract_form": AbstractFileForm})


@login_required
def update_proposal(request, proposal_id):

    proposal = ProposalModel.objects.get(id=proposal_id, author=request.user)

    if not proposal:
        return HttpResponseForbidden("Permission Denied.")

    if request.method == "POST":
        proposal_form = ProposalForm(request.POST, request.FILES,
                                     instance=proposal)
        if proposal_form.is_valid():
            proposal_form.save()
            message = _("Proposal updated")
            messages.add_message(request, messages.SUCCESS, message)
            return redirect(reverse("proposal:list"))
        else:
            return render(request, "proposal/create.html",
                          {"proposal_form": proposal_form})
    else:
        proposal_form = ProposalForm(instance=proposal)
        return render(request, "proposal/create.html",
                      {"proposal_form": proposal_form})


@login_required
def delete_proposal(request, proposal_id):

    if not settings.CALL_FOR_PROPOSAL:
        raise PermissionDenied("Time is up.")

    proposal = ProposalModel.objects.get(id=proposal_id, author=request.user)

    if not proposal:
        return HttpResponseForbidden("Permission Denied.")

    if request.method == "POST":
        proposal.delete()
        return redirect(reverse("proposal:list"))

    else:
        return HttpResponseNotAllowed("")


@login_required
def upload_abstract(request, proposal_id):

    if request.method == "POST":

        abstract_file, success = \
            AbstractFile.objects.get_or_create(proposal_id=proposal_id)

        abstract_file_form = AbstractFileForm(request.POST, request.FILES,
                                              instance=abstract_file)

        if abstract_file_form.is_valid():
            abstract_file_form.save()
        else:
            for field, message in abstract_file_form.errors.items():
                messages.add_message(request, messages.ERROR, message)

        return redirect(reverse("proposal:list"))
    else:
        return HttpResponseNotAllowed("")
