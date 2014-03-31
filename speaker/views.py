# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404

from proposal.models import ProposalModel


def _get_author_of_accept_proposals():
    author_of_accept_proposals = ProposalModel.objects \
        .filter(result__decision=1) \
        .values_list("author", flat=True) \
        .order_by('author__first_name')
    return author_of_accept_proposals


def list_speakers(request):
    author_of_accept_proposals = _get_author_of_accept_proposals()
    speakers = User.objects.filter(id__in=author_of_accept_proposals)
    return render(request, "list_speakers.html", {"speakers": speakers})


def speaker_info(request, speaker_id):
    author_of_accept_proposals = _get_author_of_accept_proposals()
    if not int(speaker_id) in author_of_accept_proposals:
        raise Http404

    speaker = User.objects.get(id=speaker_id)
    profile = speaker.get_profile()
    picture = profile.picture
    og_image_url = picture.url if picture else None
    return render(request, "speaker_info.html",
                  {"speaker": speaker,
                   "profile": profile,
                   "og_image_url": og_image_url})
