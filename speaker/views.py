# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404


def _get_author_of_accept_proposals():
    return User.objects.filter(proposals__result__decision=1)


def list_speakers(request):
    speakers = _get_author_of_accept_proposals().order_by('first_name')
    return render(request, "list_speakers.html", {"speakers": speakers})


def speaker_info(request, speaker_id):
    try:
        speaker = _get_author_of_accept_proposals().get(id=speaker_id)
    except User.DoesNotExist:
        raise Http404

    profile = speaker.get_profile()
    picture = profile.picture
    og_image_url = picture.url if picture else None
    return render(request, "speaker_info.html",
                  {"speaker": speaker,
                   "profile": profile,
                   "og_image_url": og_image_url})
