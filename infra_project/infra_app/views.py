from django.http import HttpResponse


def index(request):
    return HttpResponse("Ура! У меня всё получилось!")


def second_page(request):
    return HttpResponse("А это вторая страница!")
