# -*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import render
from proposal.models import ProposalModel


def _get_accepted_proposals():
    return ProposalModel.objects.filter(result__decision=1) \
        .select_related('author')


def show(request, page='show'):

    data = {'page': page}

    if request.is_ajax():
        template = 'demo/' + page + '_content.html'
    else:
        template = 'demo/' + page + '.html'

    return render(request, template, data)


def proposal_content(request, proposal_id):
    try:
        proposal = ProposalModel.objects.get(id=int(proposal_id))
    except ProposalModel.DoesNotExist:
        raise Http404

    profile = proposal.author.get_profile()
    picture = profile.picture
    og_image_url = picture.url if picture else None

    data = {
        'proposal': proposal,
        'profile': profile,
        "og_image_url": og_image_url,
    }

    if request.is_ajax():
        template = 'demo/talk_content.html'
    else:
        template = 'demo/talk.html'

    return render(request, template, data)


def program(request):
    programs = {}

    accepted_proposals = {p.id: p for p in _get_accepted_proposals()}
    print accepted_proposals.keys()

    day1_programs_id = (
        30, 71, 88, 73, 
        55, 102, 93, 29, 
        81, 51, 35, 6, 

        96, 66, 74, 78, 
        60, 64, 65, 
        58, 69, 7 
    )
    day2_programs_id = (
        97, 99, 53, 67, 
        70, 28, 95, 40, 
        63, 101, 31, 75, 

        45, 54, 61, 
        41, 36, 46, 44, 
        84, 37, 38 
    )
    programs = (
        {pid: accepted_proposals[pid] for pid in day1_programs_id},
        {pid: accepted_proposals[pid] for pid in day2_programs_id}
    )

    data = {'programs': programs}
    return render(request, 'demo/program.html', data)
