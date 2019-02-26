from django.shortcuts import render


def show_source(request):
    return render(request, 'json_source.html')


def show_dest(request):
    return render(request, 'json_dest.html')


def show_ws_source(request):
    return render(request, 'ws_source.html')


def show_ws_dest(request):
    return render(request, 'ws_dest.html')