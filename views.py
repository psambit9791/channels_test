from django.shortcuts import render


def show_source(request):
    return render(request, 'source.html')


def show_dest(request):
    return render(request, 'dest.html')