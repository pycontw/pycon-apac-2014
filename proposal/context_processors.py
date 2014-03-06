from django.conf import settings


def cfp(request):

    return {"CALL_FOR_PROPOSAL": settings.CALL_FOR_PROPOSAL}
