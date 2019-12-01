from django.shortcuts import render


def index(request):

    template_name = "core/main.html"
    context = {}
    return render(request, template_name, context)
