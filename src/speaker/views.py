# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from proposal.models import ProposalModel


def _get_author_of_accepted_proposals():
    return User.objects.filter(proposals__result__decision=1).distinct()


def list_speakers(request):
    speakers = _get_author_of_accepted_proposals().order_by('first_name')
    return render(request, "list_speakers.html", {"speakers": speakers})


def speaker_info(request, speaker_id):
    try:
        speaker = _get_author_of_accepted_proposals().get(id=speaker_id)
    except User.DoesNotExist:
        raise Http404

    profile = speaker.get_profile()
    proposals = ProposalModel.objects.filter(author=speaker,
                                             result__decision=1)
    picture = profile.picture
    og_image_url = picture.url if picture else None
    return render(request, "speaker_info.html",
                  {"speaker": speaker,
                   "profile": profile,
                   "proposals": proposals,
                   "og_image_url": og_image_url})
