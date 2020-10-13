from django.http import HttpResponse


def alive_view(request):
    return HttpResponse("I'm alive...")
    