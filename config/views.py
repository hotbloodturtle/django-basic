from django.http import HttpResponse


def alive_view(request):
    a = 1
    return HttpResponse("I'm alive...")
    