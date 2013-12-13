from django.shortcuts import HttpResponse, render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .forms import ProposalForm
from .models import ProposalModel


@login_required
def create_proposal(request):

    if request.method == "POST":

        proposal_form = ProposalForm(request.POST)

        if proposal_form.is_valid():
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
def update_proposal(request):

    return HttpResponse("")


@login_required
def delete_proposal(request):

    return HttpResponse("")
