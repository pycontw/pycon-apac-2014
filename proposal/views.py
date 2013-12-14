from django.shortcuts import HttpResponse, render, redirect
from django.http import HttpResponseNotAllowed, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .forms import ProposalForm
from .models import ProposalModel


@login_required
def create_proposal(request):

    if request.method == "POST":

        proposal_form = ProposalForm(request.POST, request.FILES)

        if proposal_form.is_valid():
            proposal = proposal_form.save(commit=False)
            proposal.author = request.user
            proposal.save()
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
    return render(request, "proposal/list.html", {"my_proposal": my_proposal})


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

    proposal = ProposalModel.objects.get(id=proposal_id, author=request.user)

    if not proposal:
        return HttpResponseForbidden("Permission Denied.")

    if request.method == "POST":
        proposal.delete()
        return redirect(reverse("proposal:list"))

    else:
        return HttpResponseNotAllowed("")
